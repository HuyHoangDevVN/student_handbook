param(
    [string]$ConfigFile = "mkdocs-pdf.yml"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ConfigFile)) {
    throw "Khong tim thay file cau hinh PDF: $ConfigFile"
}

$env:ENABLE_PDF_EXPORT = "1"

Write-Host "Building PDF handbook with config $ConfigFile ..."
try {
    mkdocs build --strict -f $ConfigFile

    if ($LASTEXITCODE -ne 0) {
        throw "PDF build failed."
    }
}
catch {
    Write-Host ""
    Write-Host "PDF build failed."
    if ($env:GITHUB_ACTIONS -eq "true") {
        Write-Host "The PDF toolchain is available in CI, so this failure is likely caused by PDF content/config issues."
        Write-Host "Check the build log for:"
        Write-Host "  - broken links such as '#'"
        Write-Host "  - HTML/CSS that works on web but not in mkdocs-with-pdf"
        Write-Host "  - warnings promoted to errors by the PDF plugin"
    }
    else {
        Write-Host "Likely cause on Windows: missing GTK/Pango libraries required by WeasyPrint."
        Write-Host "Recommended paths:"
        Write-Host "  1. Run the build inside WSL/Ubuntu"
        Write-Host "  2. Use GitHub Actions workflow '.github/workflows/pdf-handbook.yml'"
    }
    throw
}

Write-Host "PDF build completed. Check site/pdf/student-it-handbook.pdf"
