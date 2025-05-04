# Program for note-taking app

class NoteTakingApp:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        """Adds a note to the list."""
        self.notes.append(note)
        print("Note added successfully!")

    def view_notes(self):
        """Displays all notes."""
        if not self.notes:
            print("No notes available.")
        else:
            print("\nYour Notes:")
            for idx, note in enumerate(self.notes, start=1):
                print(f"{idx}. {note}")

    def delete_note(self, note_index):
        """Deletes a note by its index."""
        if 0 <= note_index < len(self.notes):
            deleted_note = self.notes.pop(note_index)
            print(f"Deleted note: {deleted_note}")
        else:
            print("Invalid note index. Please try again.")

def display_menu():
    """Displays the menu options."""
    print("\nNote Taking App")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

def main():
    """Main function to run the note-taking app."""
    app = NoteTakingApp()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            note = input("Enter your note: ").strip()
            if note:
                app.add_note(note)
            else:
                print("Note cannot be empty. Please try again.")
        elif choice == "2":
            app.view_notes()
        elif choice == "3":
            if not app.notes:
                print("No notes available to delete.")
                continue
            try:
                note_index = int(input("Enter the note index to delete: ").strip()) - 1
                app.delete_note(note_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()