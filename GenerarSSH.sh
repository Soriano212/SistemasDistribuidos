#Crea clave ssh
ssh-keygen -t ed25519 -C "your_email@example.com"

#Comprueba si el agente ssh esta activo
Get-Service ssh-agent #Ejecuntando
Get-Process ssh-agent #Activo

#Inicia el agente si no esta activo
Start-Service ssh-agent #Ejecuta
ssh-agent #Activa

#Agregar llave ssh
ssh-add ~/.ssh/id_ed25519
