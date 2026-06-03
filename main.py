# GitHub url: https://github.com/yedidya-ben-haim/crud_shaps_management


import logging
from shape_manager import ShapeManager


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)


def print_main_menu():
    """
        Displaying the main menu to the user
    """
    print("\n--- Shape Management System ---")
    print("1. Add shape")
    print("2. Show all shapes")
    print("3. Update shape")
    print("4. Delete shape")
    print("5. Exit")



def main():
    logger.info("The program started running.")
    manager = ShapeManager()

    while True:

        print_main_menu()

        choice = input("Enter your choice (1-5): ")

        # Option 1: Create
        if choice == '1':
            while True:
                logger.info("Add shape chosen")
                print("\nChoose a shape:")
                print("1. Square")
                print("2. Rectangle")
                print("3. Circle")
                print("4. return")
                shape_choice = input("Enter shape type (1-3) or 4 for Exit: ")
                shape_id = manager.get_new_id()

                try:
                    if shape_choice == '1':
                        side = float(input("Enter side length: "))
                        shape_dic = {"id": shape_id,"shape_type": "square", "side": side}


                    elif shape_choice == '2':
                        width = float(input("Enter width: "))
                        height = float(input("Enter height: "))
                        shape_dic = {"id": shape_id, "shape_type": "rectangle","width": width, "height": height}

                    elif shape_choice == '3':
                        radius = float(input("Enter radius: "))
                        shape_dic = {"id": shape_id, "shape_type": "circle", "radius": radius}
                    elif shape_choice == '4':
                        print("return")
                        break
                    else:
                        print("Invalid choice.")
                        continue  # Returns to the start of the while loop
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
                    continue

                try:# Passing the dictionary to our completed create_shape function
                    created_shape = manager.create_shape(shape_dic)
                    if created_shape:
                        print("Shape added successfully!")
                        break

                except ValueError:
                    print("Invalid input! Please enter numbers only.")

        # Option 2: Read
        elif choice == '2':
            logger.info("Show all shapes chosen")
            manager.get_all_shapes()

        # Option 3: Update
        elif choice == '3':
            logger.info("Update shape chosen")
            try:
                shape_id = int(input("Enter the ID of the shape to update: "))
                shape_to_update = manager.get_shape_by_id(shape_id)

                print(f"the shape to update: {shape_to_update.to_dict()}")

                if shape_to_update is not None:
                    new_data = {}
                    if shape_to_update.shape_type == "rectangle":
                        width = float(input("Enter the new side width: "))
                        height = float(input("Enter the new length: "))
                        new_data["width"] = width
                        new_data["height"] = height
                    elif shape_to_update.shape_type == "circle":
                        radius = float(input("Enter the new radius: "))
                        new_data["radius"] = radius
                    elif shape_to_update.shape_type == "square":
                        side = float(input("Enter the new side length: "))
                        new_data["side"] = side

                    updated_shape = manager.update_shape(shape_id, new_data)
                    print(f"""shape: {updated_shape.id} | type: {updated_shape.shape_type.capitalize()}
                              updated successfully
                              the new details: {updated_shape.to_dict()}""")
                else:
                    print("Shape not found.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        # Option 4: Delete
        elif choice == '4':
            logger.info("Delete shape chosen")
            try:
                shape_id = int(input("Enter the ID of the shape to delete: "))
                manager.delete_shape(shape_id)
                print(f"Shape with ID {shape_id} deleted successfully.")
            except ValueError:
                print("Invalid ID! Please enter a number.")

        # Option 5: Exit
        elif choice == '5':
            logger.info("The program was closed by the user.")
            print("Exiting the program. Goodbye!")
            manager.save_to_json()
            break  # Breaks the infinite loop and terminates the program

        # Invalid input for main menu
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()

