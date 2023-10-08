import pandas as pd
import forallpeople

forallpeople.environment("structural", top_level=True)

### Bolt Dimensions ###
bolt_dimensions_df = pd.read_excel("/Users/jlcalda/Documents/jupyter_notebooks/mercury/calcs/constants/anchor_bolt/BOLT_DIMENSIONS.xlsx", sheet_name="Sheet1", usecols="A:E", skiprows=0, nrows=21, index_col=None)

bolt_dimensions_df["DIAMETER"] = bolt_dimensions_df["DIAMETER"]*mm
bolt_dimensions_df["PITCH"] = bolt_dimensions_df["PITCH"]*mm
bolt_dimensions_df["GROSS AREA"] = bolt_dimensions_df["GROSS AREA"]*mm**2
bolt_dimensions_df["NET AREA"] = bolt_dimensions_df["NET AREA"]*mm**2

def bolt_table():
    """
    Returns a DataFrame of all bolt grades and their properties.
    """
    return bolt_dimensions_df

def bolt_diameters():
    """
    Returns a list of all bolt diameters.
    """
    return bolt_dimensions_df["TAG"].tolist()

print(bolt_diameters())
def bolt_diameter(Bolt_Tag):
    """
    Returns the dimensions of a bolt diameter.
    """
    try:
        return bolt_dimensions_df.loc[bolt_dimensions_df["TAG"] == Bolt_Tag]["DIAMETER"].iloc[0]
    except:
        raise ValueError("Diameter not found")

def bolt_pitch(Bolt_Tag):
    """
    Returns the pitch of a bolt diameter.
    """
    try:
        return bolt_dimensions_df.loc[bolt_dimensions_df["TAG"] == Bolt_Tag]["PITCH"].iloc[0]
    except:
        raise ValueError("Diameter not found")

def bolt_grossArea(Bolt_Tag):
    """
    Returns the gross area of a bolt diameter.
    """
    try:
        return bolt_dimensions_df.loc[bolt_dimensions_df["TAG"] == Bolt_Tag]["GROSS AREA"].iloc[0]
    except:
        raise ValueError("Diameter not found")

def bolt_netArea(Bolt_Tag):
    """
    Returns the net area of a bolt diameter.
    """
    try:
        return bolt_dimensions_df.loc[bolt_dimensions_df["TAG"] == Bolt_Tag]["NET AREA"].iloc[0]
    except:
        raise ValueError("Diameter not found")

### Bolt Grades ###
bolt_grades_df = pd.read_excel("/Users/jlcalda/Documents/jupyter_notebooks/mercury/calcs/constants/anchor_bolt/BOLT_GRADES.xlsx", sheet_name="Sheet1", usecols="A:C", skiprows=0, nrows=10, index_col=None)

bolt_grades_df["YIELD STRENGTH"] = bolt_grades_df["YIELD STRENGTH"]*MPa
bolt_grades_df["ULTIMATE STRENGTH"] = bolt_grades_df["ULTIMATE STRENGTH"]*MPa

def bolt_Fu(Grade):
    """
    Returns the ultimate strength of a bolt grade.
    """
    try:
        return bolt_grades_df.loc[bolt_grades_df["GRADE"] == Grade]["ULTIMATE STRENGTH"].iloc[0]
    except:
        raise ValueError("Grade not found")

def bolt_Fy(Grade):
    """
    Returns the yield strength of a bolt grade.
    """
    try:
        return bolt_grades_df.loc[bolt_grades_df["GRADE"] == Grade]["YIELD STRENGTH"].iloc[0]
    except:
        raise ValueError("Grade not found")

def bolt_grades():
    """
    Returns a list of all bolt grades.
    """
    return bolt_grades_df["GRADE"].tolist()

