$ErrorActionPreference = "Stop"

$generator = Join-Path $PSScriptRoot "scripts/create-starter-pack.py"

if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $generator @args
    exit $LASTEXITCODE
}

if (Get-Command python3 -ErrorAction SilentlyContinue) {
    & python3 $generator @args
    exit $LASTEXITCODE
}

if (Get-Command python -ErrorAction SilentlyContinue) {
    & python $generator @args
    exit $LASTEXITCODE
}

Write-Error "Python 3 is required to create an AIPOM Starter Pack. Install Python 3, then run this command again."
exit 1
