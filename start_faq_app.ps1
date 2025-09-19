# Employee FAQ Application Launcher
Write-Host "Starting Employee FAQ Application..." -ForegroundColor Green
Write-Host "Server will start at: http://localhost:8080" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Red
Write-Host ""

# Start the Flask app in background
$job = Start-Job -ScriptBlock { 
    Set-Location "C:\Users\deanw\OneDrive\Desktop\ServiceNow_website"
    python app.py 
}

# Wait a moment for server to start
Start-Sleep -Seconds 3

# Open browser automatically
Write-Host "Opening browser..." -ForegroundColor Cyan
Start-Process "http://localhost:8080"

# Keep script running and show server status
Write-Host "Server is running! Close this window to stop the server." -ForegroundColor Green
Write-Host "Or press Ctrl+C to stop gracefully." -ForegroundColor Yellow

try {
    # Keep the job running
    Wait-Job $job
}
finally {
    # Clean up
    Remove-Job $job -Force
}