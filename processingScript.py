#Google CameraTrapAI Post-Processing Script
#Created by Lukas Kopacki, ArborVox

#Install dependencies. Use 'pip install [package]'
#if a message indicates the library does not exist
import json
import pandas as pd
import os
import shutil
from pathlib import Path

######################################
#### INPUT Your desired paths here######

#This should be the path to the JSON output from the model
json_file = r"Example.json"
#thihs should be the desired path to your photo summary
output_xlsx= r"Example_Path\photo_report.xlsx"
#This should be the path to where you want the species-sorted folders to wind up
output_dir = r"ExamplePath\Sorted"
##################
#########################################

def extract_filename(filepath):
    """Extract the filename from the full path (everything after the last /)"""
    
    return filepath.split('/')[-1]

def extract_prediction_text(prediction):
    """Extract everything to the right of the third-to-last semicolon"""
    # Split the string by semicolons
    parts = prediction.split(';')
    
    # If we have at least 3 parts, return the last element
    if len(parts) >= 3:
        return parts[-1]
    else:
        # If there aren't enough semicolons, return the original
        return prediction

def process_json_to_excel(json_data, output_xlsx):
    """
    Process the JSON data and extract filepath, prediction, and prediction_score
    Convert to Excel file
    """
    # Parse the JSON data
    data = json.loads(json_data) if isinstance(json_data, str) else json_data
    
    # Extract required fields
    results = []
    for entry in data["predictions"]:
        try:
            print(entry)
            results.append({
                "filename": extract_filename(entry["filepath"]),
                "prediction": extract_prediction_text(entry["prediction"]),
                "prediction_score": entry["prediction_score"]})
        except:
            print("error")
            continue
        
    
    # Convert to DataFrame
    df = pd.DataFrame(results)
    
    # Save to Excel
    df.to_excel(output_xlsx, index=False)
    print(f"Data successfully exported to {output_xlsx}")
    
    return df

def sort_images_by_species(json_file, output_dir="sorted species"):
    # Load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Create the main output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created main output directory: {output_dir}")
    
    # Process each prediction
    for item in data.get('predictions', []):
        filepath = item.get('filepath')
        prediction = item.get('prediction')
        
        if not filepath or not prediction:
            continue
        
        # Extract the species name (text after the last semicolon)
        parts = prediction.split(';')
        if len(parts) > 1:
            species = parts[-1].strip()
        else:
            species = "unknown"
        
        # Create species directory if it doesn't exist
        species_dir = os.path.join(output_dir, species)
        if not os.path.exists(species_dir):
            os.makedirs(species_dir)
            print(f"Created species directory: {species_dir}")
        
        # Get the filename from the filepath
        filename = os.path.basename(filepath)
        
        # Define the source and destination paths
        source_path = filepath
        dest_path = os.path.join(species_dir, filename)
        
        # Copy the file (use shutil.copy2 to preserve metadata)
        try:
            # For safety, check if the source file exists before attempting to copy
            if os.path.exists(source_path):
                shutil.copy2(source_path, dest_path)
                print(f"Copied {filename} to {species_dir}")
            else:
                # If the exact path doesn't exist, try finding the file by name in the current directory
                base_filename = os.path.basename(source_path)
                if os.path.exists(base_filename):
                    shutil.copy2(base_filename, dest_path)
                    print(f"Copied {base_filename} to {species_dir}")
                else:
                    print(f"Warning: Source file not found: {source_path}")
        except Exception as e:
            print(f"Error copying {filename}: {e}")

def main():
    # create the excel file
    try:
        # Option 1: If you saved the JSON to a file
        with open(json_file, 'r') as f:
            json_data = json.load(f)
            process_json_to_excel(json_data, output_xlsx)
    except FileNotFoundError:
        print("JSON file not found. Make sure to save the JSON data to 'file.json' or modify the script.")
    
    # Sort the images
    sort_images_by_species(json_file, output_dir)
    print("Image sorting complete!")
        
if __name__ == "__main__":
    main()

