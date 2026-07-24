# Student Name - Neil Khan
# Date - 19 July 2026
# Program Description - Personal Task and Project Manager (Week 7 Assignment)
# Tier Level - Base Level


import sqlite3


# Function 1: create_connection(db_file)
def create_connection(db_file):
    """Create and return a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as error:
        print(f"Database connection error: {error}")
        return None


# Function 2: setup_database(conn)
def setup_database(conn):
    """Create the tasks table if it does not already exist."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Pending',
            due_date TEXT,
            project_id INTEGER
        )
        """)

        conn.commit()

    except sqlite3.Error as error:
        print(f"Database setup error: {error}")


# Function 3: add_task(conn, title, description, priority, due_date)
def add_task(conn, title, description, priority, due_date):
    """Add a new task to the database."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks
            (title, description, priority, due_date, project_id)
            VALUES (?, ?, ?, ?, ?)
        """, (title, description, priority, due_date, None))

        conn.commit()

        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding task: {error}")
        return None


# Function 4: get_all_tasks(conn)
def get_all_tasks(conn):
    """Return all tasks ordered by priority and due date."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tasks
            ORDER BY priority, due_date
        """)

        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Error retrieving tasks: {error}")
        return []


# Function 5: get_tasks_by_status(conn, status)
def get_tasks_by_status(conn, status):
    """Return all tasks with the specified status."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE status = ?
            ORDER BY priority
        """, (status,))

        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Error retrieving tasks by status: {error}")
        return []


# Function 6: update_task_status(conn, task_id, new_status)
def update_task_status(conn, task_id, new_status):
    """Update the status of a task."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks
            SET status = ?
            WHERE id = ?
        """, (new_status, task_id))

        conn.commit()

        return cursor.rowcount > 0

    except sqlite3.Error as error:
        print(f"Error updating task: {error}")
        return False


# Function 7: delete_task(conn, task_id)
def delete_task(conn, task_id):
    """Delete a task from the database."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM tasks
            WHERE id = ?
        """, (task_id,))

        conn.commit()

        return cursor.rowcount > 0

    except sqlite3.Error as error:
        print(f"Error deleting task: {error}")
        return False


# Function 8: display_tasks(tasks)
def display_tasks(tasks):
    """Display tasks in a formatted table."""

    if not tasks:
        print("No tasks found.")
        return

    print("-" * 70)
    print(f"{'ID':<4} {'Title':<25} {'Priority':<10} {'Status':<15} {'Due Date':<12}")
    print("-" * 70)

    for task in tasks:
        task_id = task[0]
        title = task[1][:25]
        priority = task[3]
        status = task[4]
        due_date = task[5]

        print(f"{task_id:<4} {title:<25} {priority:<10} {status:<15} {due_date:<12}")


# ----------------------
# Main Program
# ----------------------

def main():

    conn = create_connection("tasks.db")

    if conn is None:
        print("Unable to connect to database.")
        return

    setup_database(conn)

    print("Adding Tasks...\n")

    task1 = add_task(
        conn,
        "Update production servers",
        "Security updates and patches",
        "High",
        "2026-08-03"
    )
    print(f"Task added with ID: {task1}")

    task2 = add_task(
        conn,
        "Create user accounts",
        "New staff in HR",
        "Medium",
        "2026-08-05"
    )
    print(f"Task added with ID: {task2}")

    task3 = add_task(
        conn,
        "Update IT asset inventory",
        "Newly deployed laptops and desktops",
        "Low",
        "2026-08-11"
    )
    print(f"Task added with ID: {task3}")

    task4 = add_task(
        conn,
        "Replace UPS batteries",
        "Second floor UPS",
        "High",
        "2026-08-07"
    )
    print(f"Task added with ID: {task4}")

    task5 = add_task(
        conn,
        "Monthly backups",
        "Critical databases and applications",
        "High",
        "2026-08-28"
    )
    print(f"Task added with ID: {task5}")

    task6 = add_task(
        conn,
        "IT department meeting",
        "Discuss upcoming projects",
        "Low",
        "2026-08-24"
    )
    print(f"Task added with ID: {task6}")

    task7 = add_task(
        conn,
        "Active Directory cleanup",
        "Review and remove inactive user accounts",
        "Medium",
        "2026-08-19"
    )
    print(f"Task added with ID: {task7}")

    task8 = add_task(
        conn,
        "Helpdesk report",
        "Report on last month's helpdesk tickets",
        "Low",
        "2026-08-28"
    )
    print(f"Task added with ID: {task8}")
    print()

# List all tasks
    print("\n=== ALL TASKS ===")
    all_tasks = get_all_tasks(conn)
    display_tasks(all_tasks)
    print()

# List pending tasks
    print("\n=== PENDING TASKS ===")
    pending_tasks = get_tasks_by_status(conn, "Pending")
    display_tasks(pending_tasks)
    print()

# Update task status
    print("\nUpdating Task Status...")
    updated = update_task_status(conn, task4, "In Progress")

    if updated:
        print(f"Status updated for task {task4}.")
    else:
        print("Task not found.")

# Delete task
    print("\nDeleting Task...")
    deleted = delete_task(conn, task6)

    if deleted:
        print(f"Task {task6} deleted.")
    else:
        print("Task not found.")
    print()

# List remaining tasks
    print("\n=== FINAL TASK LIST ===")
    all_tasks = get_all_tasks(conn)
    display_tasks(all_tasks)
    print()

    conn.close()


if __name__ == "__main__":
    main()