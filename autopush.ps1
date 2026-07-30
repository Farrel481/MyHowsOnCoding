param(
  [string]$Repo = "C:\Users\Farrel Satriano\MyHowsOnCoding",
  [string]$Branch = "main",
  [int]$CheckEverySeconds = 10 #Editable
)

Set-Location -LiteralPath $Repo
Write-Host "Watching $Repo. Press Ctrl+C to stop."

while ($true) {
  $changes = git status --porcelain

  if ($changes) {
    Write-Host "Changes found. Committing and pushing..." -ForegroundColor Yellow
    git add -A
    $message = "Auto update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    git commit -m $message

    if ($LASTEXITCODE -eq 0) {
      git push origin $Branch
      if ($LASTEXITCODE -eq 0) {
        Write-Host "Pushed successfully." -ForegroundColor Green
      } else {
        Write-Host "Push failed. Read the Git error above." -ForegroundColor Red
      }
    } else {
      Write-Host "Commit failed. Read the Git error above." -ForegroundColor Red
    }
  }

  Start-Sleep -Seconds $CheckEverySeconds
}