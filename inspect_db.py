# inspect_db.py
from database import engine
from sqlalchemy import inspect

def inspect_database():
    try:
        print("🔍 Inspecting database structure...")
        
        # Create an inspector
        inspector = inspect(engine)
        
        # Get all table names
        table_names = inspector.get_table_names()
        print("✅ Tables in database:", table_names)
        
        # If we found tables, show their columns
        if table_names:
            for table_name in table_names:
                print(f"\n📊 Columns in table '{table_name}':")
                
                columns = inspector.get_columns(table_name)
                for column in columns:
                    # Get additional column info
                    nullable = "NULL" if column['nullable'] else "NOT NULL"
                    primary_key = "PRIMARY KEY" if column.get('primary_key', False) else ""
                    default = f"DEFAULT {column['default']}" if column['default'] is not None else ""
                    
                    print(f"  - {column['name']}: {column['type']} {nullable} {primary_key} {default}".strip())
                    
                # Also show primary keys and indexes for each table
                print(f"\n  🔑 Primary keys for '{table_name}':")
                pk_constraint = inspector.get_pk_constraint(table_name)
                print(f"    {pk_constraint['constrained_columns']}")
                
                print(f"\n  📑 Indexes for '{table_name}':")
                indexes = inspector.get_indexes(table_name)
                for index in indexes:
                    print(f"    - {index['name']}: {index['column_names']} (unique: {index.get('unique', False)})")
                    
        else:
            print("❌ No tables found in the database.")
            
    except Exception as e:
        print(f"❌ Error during inspection: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    inspect_database()