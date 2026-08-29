[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$importRoot = Join-Path $repoRoot 'ets-import'

$canonicalFiles = @(
    'gruppenadressen.xml',
    'gruppenadressen-komplett.xml',
    'gruppenadressen-abstellkammer.xml',
    'gruppenadressen-zentral-zeit.xml',
    'gruppenadressen-sicherheit.xml',
    'gruppenadressen-reparatur-safe-rauchwarnmelder.xml',
    'gruppenadressen-raumcontroller.xml',
    'gruppenadressen-waermepumpe.xml'
)

$errors = [System.Collections.Generic.List[string]]::new()
$allEntries = [System.Collections.Generic.List[object]]::new()
$entriesByFile = @{}

foreach ($fileName in $canonicalFiles) {
    $path = Join-Path $importRoot $fileName
    if (-not (Test-Path -LiteralPath $path)) {
        $errors.Add("Fehlende Importdatei: $fileName")
        continue
    }

    try {
        [xml]$xml = Get-Content -LiteralPath $path -Raw
    }
    catch {
        $errors.Add("Ungültiges XML in ${fileName}: $($_.Exception.Message)")
        continue
    }

    $nodes = $xml.SelectNodes("//*[local-name()='GroupAddress']")
    $fileEntries = [System.Collections.Generic.List[object]]::new()
    foreach ($node in $nodes) {
        $entry = [pscustomobject]@{
            File = $fileName
            Address = [string]$node.Address
            Name = [string]$node.Name
            DPT = [string]$node.DPTs
        }
        $fileEntries.Add($entry)
        $allEntries.Add($entry)
    }
    $entriesByFile[$fileName] = $fileEntries

    $duplicates = $fileEntries | Group-Object Address | Where-Object Count -gt 1
    foreach ($duplicate in $duplicates) {
        $errors.Add("Doppelte Adresse $($duplicate.Name) in $fileName")
    }
}

foreach ($addressGroup in ($allEntries | Group-Object Address)) {
    $names = @($addressGroup.Group.Name | Sort-Object -Unique)
    if ($names.Count -gt 1) {
        $details = $addressGroup.Group | ForEach-Object { "$($_.File)='$($_.Name)'" }
        $errors.Add("Namenskonflikt $($addressGroup.Name): $($details -join ', ')")
    }

    $dpts = @($addressGroup.Group.DPT | Where-Object { $_ } | Sort-Object -Unique)
    if ($dpts.Count -gt 1) {
        $details = $addressGroup.Group | ForEach-Object { "$($_.File)='$($_.DPT)'" }
        $errors.Add("DPT-Konflikt $($addressGroup.Name): $($details -join ', ')")
    }
}

$expectedSecurity = [ordered]@{
    '10/0/0' = @('Sicherheitsmodus Status', 'DPST-1-11')
    '10/0/1' = @('Sicherheitsmodus Alarm', 'DPST-1-5')
    '10/0/2' = @('Sicherheitsmodul In Betrieb', 'DPST-1-11')
    '10/0/3' = @('Sicherheitsmodus Befehl Passwort', 'DPST-16-0')
    '10/0/4' = @('Sicherheitsmodus Alarm quittieren', 'DPST-1-1')
    '10/0/5' = @('Sicherheitsmodus Aktivieren', 'DPST-1-1')
    '10/1/0' = @('Rauchalarm', 'DPST-1-2')
    '10/1/1' = @('Rauchwarnmelder Störung', 'DPST-1-2')
    '10/1/2' = @('Rauchwarnmelder Batterie schwach', 'DPST-1-2')
    '10/1/4' = @('Rauchwarnmelder Testalarm auslösen', 'DPST-1-3')
    '10/1/5' = @('Rauchwarnmelder Testalarm Status', 'DPST-1-2')
    '10/1/6' = @('Rauchwarnmelder Störung Rauchkammer', 'DPST-1-2')
}

$securityFiles = @(
    'gruppenadressen-komplett.xml',
    'gruppenadressen-sicherheit.xml',
    'gruppenadressen-reparatur-safe-rauchwarnmelder.xml'
)

foreach ($fileName in $securityFiles) {
    if (-not $entriesByFile.ContainsKey($fileName)) {
        continue
    }
    $entries = $entriesByFile[$fileName]
    foreach ($address in $expectedSecurity.Keys) {
        $expected = $expectedSecurity[$address]
        $actual = @($entries | Where-Object Address -eq $address)
        if ($actual.Count -ne 1) {
            $errors.Add("$fileName muss $address genau einmal enthalten")
            continue
        }
        if ($actual[0].Name -ne $expected[0] -or $actual[0].DPT -ne $expected[1]) {
            $errors.Add("Falsche Sicherheitszuordnung in $fileName für ${address}: '$($actual[0].Name)' / '$($actual[0].DPT)'")
        }
    }

    foreach ($entry in ($entries | Where-Object Address -like '10/0/*')) {
        if ($entry.Name -match 'Rauch') {
            $errors.Add("Rauchwarnmelder darf nicht unter 10/0 liegen: $fileName $($entry.Address)")
        }
    }
    foreach ($entry in ($entries | Where-Object Address -like '10/1/*')) {
        if ($entry.Name -notmatch 'Rauch') {
            $errors.Add("Unter 10/1 ist nur Rauchwarnmelder-Planung zulässig: $fileName $($entry.Address)")
        }
    }
}

$expectedCounts = @{
    'gruppenadressen-komplett.xml' = 174
    'gruppenadressen-waermepumpe.xml' = 43
    'gruppenadressen-sicherheit.xml' = 12
    'gruppenadressen-reparatur-safe-rauchwarnmelder.xml' = 12
}

foreach ($fileName in $expectedCounts.Keys) {
    if ($entriesByFile.ContainsKey($fileName)) {
        $actualCount = $entriesByFile[$fileName].Count
        if ($actualCount -ne $expectedCounts[$fileName]) {
            $errors.Add("Unerwartete Anzahl in ${fileName}: $actualCount statt $($expectedCounts[$fileName])")
        }
    }
}

if ($errors.Count -gt 0) {
    Write-Error ("Gruppenadressprüfung fehlgeschlagen:`n- " + ($errors -join "`n- "))
}

Write-Output 'Gruppenadressprüfung erfolgreich.'
foreach ($fileName in $canonicalFiles) {
    if ($entriesByFile.ContainsKey($fileName)) {
        Write-Output ("{0}: {1} Adressen" -f $fileName, $entriesByFile[$fileName].Count)
    }
}
