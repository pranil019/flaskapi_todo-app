from app import app, db

# Create all database tables
with app.app_context():
    db.create_all()
    print("✓ Database created successfully!")
    print("✓ todo.db file created in instance/ folder")
