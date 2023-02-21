import os

folders = os.listdir("carapp")

if "export" not in folders:
    print("Folder 'export' not yet created")
    print("📁 Creating...")
    print("✅ Created 'export' folder")
    os.mkdir("export")


# also check if the license folder exists
if not os.path.exists("carapp/export/plates"):
    print("📂'plates' folder does not exist yet")
    print("🛠 Creating....")
    os.makedirs("carapp/export/plates", exist_ok=True)
    print("✅ Created 'plate' folder")