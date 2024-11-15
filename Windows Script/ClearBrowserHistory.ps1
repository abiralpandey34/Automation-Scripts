# Dont' ask me why i made it.. But this script clears browsing history. 

# Warning: Everything is cleared. Don't run without looking at the code. 

$chromePath = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default"
Remove-Item -Path "$chromePath\History" -Force
Remove-Item -Path "$chromePath\Cookies" -Force
Remove-Item -Path "$chromePath\Cache" -Force

# $firefoxPath = "$env:APPDATA\Mozilla\Firefox\Profiles"
# $firefoxProfiles = Get-ChildItem -Path $firefoxPath -Directory | Where-Object { $_.Name -like '*default*' }
# foreach ($profile in $firefoxProfiles) {
#     $firefoxDB = Join-Path -Path $profile.FullName -ChildPath "places.sqlite"
#     Remove-Item -Path $firefoxDB -Force
# }

# Firefox doesn't seem to work - Will work on it later on. 

$edgePath = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default"
Remove-Item -Path "$edgePath\History" -Force
Remove-Item -Path "$edgePath\Cookies" -Force
Remove-Item -Path "$edgePath\Cache" -Force


Write-Output "Everything Cleared Boss ! "