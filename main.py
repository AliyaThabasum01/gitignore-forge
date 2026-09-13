from templates import TEMPLATES

print("🔥 GitIgnore Forge")
print("=" * 35)

print("\nAvailable project types:")
for name in TEMPLATES:
    print(f"- {name}")

choice = input("\nChoose project type: ").strip().lower()

if choice not in TEMPLATES:
    print("❌ Unknown project type.")
else:
    filename = ".gitignore"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(TEMPLATES[choice])

    print(f"\n✅ {filename} generated for {choice} project!")
