
def calculate_statistics(df):
    """Calculate summary statistics for student marks."""

    stats = {
        "average": df["Marks"].mean(),
        "highest": df["Marks"].max(),
        "lowest": df["Marks"].min(),
        "passed": (df["Marks"] >= 40).sum(),
        "failed": (df["Marks"] < 40).sum(),
    }

    return stats
