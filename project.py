# ============================================================
# APP ADDICTION RISK PREDICTOR
# Complete Dataset using:
# Dictionary + Tuple + Set + List
# ============================================================


# ------------------------------------------------------------
# 1. USER DATASET
# Tuple = fixed user information
# ------------------------------------------------------------

users = {
    101: (
        "Rahul",
        21,
        "Student",
        "Android"
    ),

    102: (
        "Anjali",
        20,
        "Student",
        "iPhone"
    ),

    103: (
        "Arun",
        25,
        "Employee",
        "Android"
    ),

    104: (
        "Meera",
        19,
        "Student",
        "iPhone"
    ),

    105: (
        "Vishnu",
        28,
        "Employee",
        "Android"
    )
}


# ------------------------------------------------------------
# 2. APP DATASET
# Dictionary = app information
#
# usage tuple:
# (screen_time, sessions, average_session, night_usage)
# ------------------------------------------------------------

apps = {

    "Instagram": {
        "category": "Social Media",
        "usage": (240, 35, 6.8, 75)
    },

    "YouTube": {
        "category": "Entertainment",
        "usage": (180, 20, 9.0, 45)
    },

    "WhatsApp": {
        "category": "Communication",
        "usage": (90, 25, 3.6, 10)
    },

    "Facebook": {
        "category": "Social Media",
        "usage": (150, 18, 8.3, 35)
    },

    "TikTok": {
        "category": "Short Video",
        "usage": (300, 50, 6.0, 100)
    },

    "Netflix": {
        "category": "Entertainment",
        "usage": (210, 8, 26.3, 80)
    },

    "Spotify": {
        "category": "Entertainment",
        "usage": (120, 15, 8.0, 20)
    },

    "PUBG": {
        "category": "Gaming",
        "usage": (270, 12, 22.5, 90)
    },

    "Snapchat": {
        "category": "Social Media",
        "usage": (160, 30, 5.3, 40)
    },

    "Amazon": {
        "category": "Shopping",
        "usage": (45, 5, 9.0, 5)
    }
}


# ------------------------------------------------------------
# 3. UNIQUE APP CATEGORIES
# Set = stores unique values
# ------------------------------------------------------------

app_categories = {
    "Social Media",
    "Entertainment",
    "Communication",
    "Short Video",
    "Gaming",
    "Shopping",
    "Education",
    "Productivity"
}


# ------------------------------------------------------------
# 4. HIGH-RISK APP CATEGORIES
# Set = unique high-risk categories
# ------------------------------------------------------------

high_risk_categories = {
    "Social Media",
    "Short Video",
    "Gaming",
    "Entertainment"
}


# ------------------------------------------------------------
# 5. RISK FACTORS
# Set = prevents duplicate risk factors
# ------------------------------------------------------------

risk_factors = {
    "High Screen Time",
    "Frequent Sessions",
    "Long Sessions",
    "Night Usage",
    "Excessive Notifications",
    "Increasing Usage",
    "Difficulty Controlling Usage"
}


# ------------------------------------------------------------
# 6. RECOMMENDATIONS
# Tuple = fixed recommendations
# ------------------------------------------------------------

recommendations = (
    "Reduce daily screen time",
    "Disable unnecessary notifications",
    "Avoid using apps before sleeping",
    "Take regular screen breaks",
    "Set daily app limits",
    "Keep the phone away during study/work",
    "Avoid continuous usage for long periods"
)


# ------------------------------------------------------------
# 7. USER-SPECIFIC USAGE DATASET
#
# Dictionary
#     user ID
#         app
#             usage tuple
# ------------------------------------------------------------

user_usage = {

    101: {
        "Instagram": (240, 35, 6.8, 75),
        "YouTube": (180, 20, 9.0, 45),
        "WhatsApp": (90, 25, 3.6, 10),
        "PUBG": (270, 12, 22.5, 90)
    },

    102: {
        "Instagram": (120, 18, 6.7, 20),
        "YouTube": (100, 12, 8.3, 15),
        "WhatsApp": (80, 20, 4.0, 5),
        "Netflix": (90, 4, 22.5, 10)
    },

    103: {
        "Instagram": (90, 12, 7.5, 15),
        "YouTube": (120, 10, 12.0, 20),
        "WhatsApp": (60, 15, 4.0, 5),
        "Spotify": (100, 12, 8.3, 10)
    },

    104: {
        "TikTok": (300, 50, 6.0, 100),
        "Instagram": (250, 40, 6.3, 90),
        "YouTube": (180, 20, 9.0, 60),
        "Snapchat": (160, 30, 5.3, 40)
    },

    105: {
        "YouTube": (80, 8, 10.0, 10),
        "WhatsApp": (50, 10, 5.0, 5),
        "Spotify": (70, 8, 8.8, 5),
        "Amazon": (45, 5, 9.0, 5)
    }
}


# ------------------------------------------------------------
# 8. NOTIFICATION DATASET
# Dictionary
# ------------------------------------------------------------

notifications = {

    101: {
        "received": 150,
        "opened": 125
    },

    102: {
        "received": 90,
        "opened": 60
    },

    103: {
        "received": 70,
        "opened": 40
    },

    104: {
        "received": 200,
        "opened": 180
    },

    105: {
        "received": 50,
        "opened": 25
    }
}


# ------------------------------------------------------------
# 9. WEEKLY USAGE DATASET
# List = collection of daily values
# ------------------------------------------------------------

weekly_usage = {

    101: [180, 200, 210, 230, 240, 260, 270],

    102: [90, 95, 100, 105, 110, 115, 120],

    103: [70, 75, 80, 85, 90, 95, 100],

    104: [180, 200, 220, 250, 270, 290, 300],

    105: [40, 45, 50, 55, 60, 65, 70]
}


# ============================================================
# RISK PREDICTION FUNCTIONS
# ============================================================


def calculate_user_usage(user_id):
    """
    Calculate total usage and other statistics
    for a particular user.
    """

    if user_id not in user_usage:
        return None

    total_screen_time = 0
    total_sessions = 0
    total_night_usage = 0

    for app, usage in user_usage[user_id].items():

        screen_time = usage[0]
        sessions = usage[1]
        night_usage = usage[3]

        total_screen_time += screen_time
        total_sessions += sessions
        total_night_usage += night_usage

    return (
        total_screen_time,
        total_sessions,
        total_night_usage
    )


def calculate_notification_rate(user_id):

    received = notifications[user_id]["received"]
    opened = notifications[user_id]["opened"]

    if received == 0:
        return 0

    return (opened / received) * 100


def calculate_usage_increase(user_id):

    data = weekly_usage[user_id]

    first_day = data[0]
    last_day = data[-1]

    if first_day == 0:
        return 0

    increase = ((last_day - first_day) / first_day) * 100

    return increase


def find_risk_factors(user_id):

    factors = set()

    usage = calculate_user_usage(user_id)

    total_screen_time = usage[0]
    total_sessions = usage[1]
    total_night_usage = usage[2]

    # High screen time
    if total_screen_time >= 500:
        factors.add("High Screen Time")

    # Frequent sessions
    if total_sessions >= 60:
        factors.add("Frequent Sessions")

    # Night usage
    if total_night_usage >= 100:
        factors.add("Night Usage")

    # Notification behavior
    notification_rate = calculate_notification_rate(user_id)

    if notification_rate >= 75:
        factors.add("Excessive Notifications")

    # Increasing usage
    usage_increase = calculate_usage_increase(user_id)

    if usage_increase >= 30:
        factors.add("Increasing Usage")

    # High-risk category
    for app in user_usage[user_id]:

        category = apps[app]["category"]

        if category in high_risk_categories:
            factors.add("High-Risk App Category")

    return factors


def calculate_risk_score(user_id):

    score = 0

    usage = calculate_user_usage(user_id)

    total_screen_time = usage[0]
    total_sessions = usage[1]
    total_night_usage = usage[2]

    # --------------------------------
    # Screen time score
    # --------------------------------

    if total_screen_time >= 700:
        score += 35

    elif total_screen_time >= 500:
        score += 25

    elif total_screen_time >= 300:
        score += 15

    elif total_screen_time >= 150:
        score += 5


    # --------------------------------
    # Session score
    # --------------------------------

    if total_sessions >= 80:
        score += 25

    elif total_sessions >= 60:
        score += 20

    elif total_sessions >= 40:
        score += 10

    elif total_sessions >= 20:
        score += 5


    # --------------------------------
    # Night usage score
    # --------------------------------

    if total_night_usage >= 200:
        score += 25

    elif total_night_usage >= 100:
        score += 15

    elif total_night_usage >= 50:
        score += 10

    elif total_night_usage >= 20:
        score += 5


    # --------------------------------
    # Usage growth score
    # --------------------------------

    usage_increase = calculate_usage_increase(user_id)

    if usage_increase >= 50:
        score += 15

    elif usage_increase >= 30:
        score += 10

    elif usage_increase >= 15:
        score += 5


    # Maximum score = 100
    if score > 100:
        score = 100

    return score


def get_risk_level(score):

    if score <= 30:
        return "Low Risk"

    elif score <= 60:
        return "Moderate Risk"

    elif score <= 80:
        return "High Risk"

    else:
        return "Very High Risk"


# ============================================================
# DISPLAY USER INFORMATION
# ============================================================


def display_user(user_id):

    if user_id not in users:
        print("User not found.")
        return

    name, age, occupation, device = users[user_id]

    print("\n======================================")
    print("          USER INFORMATION")
    print("======================================")

    print("User ID     :", user_id)
    print("Name        :", name)
    print("Age         :", age)
    print("Occupation  :", occupation)
    print("Device      :", device)


# ============================================================
# DISPLAY USAGE INFORMATION
# ============================================================


def display_usage(user_id):

    if user_id not in user_usage:
        print("Usage data not found.")
        return

    print("\n======================================")
    print("          APP USAGE DATA")
    print("======================================")

    for app, usage in user_usage[user_id].items():

        screen_time = usage[0]
        sessions = usage[1]
        average_session = usage[2]
        night_usage = usage[3]

        print("\nApp:", app)
        print("Category:", apps[app]["category"])
        print("Screen Time:", screen_time, "minutes")
        print("Sessions:", sessions)
        print("Average Session:", average_session, "minutes")
        print("Night Usage:", night_usage, "minutes")


# ============================================================
# DISPLAY PREDICTION
# ============================================================


def display_prediction(user_id):

    score = calculate_risk_score(user_id)

    level = get_risk_level(score)

    factors = find_risk_factors(user_id)

    usage = calculate_user_usage(user_id)

    print("\n======================================")
    print("       ADDICTION RISK PREDICTION")
    print("======================================")

    print("User ID:", user_id)

    print("Total Screen Time:",
          usage[0], "minutes")

    print("Total Sessions:",
          usage[1])

    print("Night Usage:",
          usage[2], "minutes")

    print("Risk Score:",
          score, "/ 100")

    print("Risk Level:",
          level)

    print("\nRisk Factors:")

    if len(factors) == 0:
        print("No major risk factors detected.")

    else:
        for factor in factors:
            print("-", factor)

    print("\nRecommendations:")

    if score > 30:

        for recommendation in recommendations:
            print("-", recommendation)

    else:

        print("- Continue maintaining healthy app usage.")


# ============================================================
# DISPLAY ALL USERS
# ============================================================


def display_all_users():

    print("\n======================================")
    print("             ALL USERS")
    print("======================================")

    for user_id, data in users.items():

        name = data[0]
        age = data[1]
        occupation = data[2]

        score = calculate_risk_score(user_id)
        level = get_risk_level(score)

        print(
            user_id,
            "|",
            name,
            "| Age:",
            age,
            "|",
            occupation,
            "| Score:",
            score,
            "|",
            level
        )


# ============================================================
# MAIN MENU
# ============================================================


def main():

    while True:

        print("\n")
        print("==============================================")
        print("       APP ADDICTION RISK PREDICTOR")
        print("==============================================")

        print("1. Display All Users")
        print("2. Display User Information")
        print("3. Display App Usage")
        print("4. Predict Addiction Risk")
        print("5. Display App Categories")
        print("6. Display High-Risk Categories")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        # ----------------------------------------
        # Option 1
        # ----------------------------------------

        if choice == "1":

            display_all_users()


        # ----------------------------------------
        # Option 2
        # ----------------------------------------

        elif choice == "2":

            try:
                user_id = int(input("Enter User ID: "))
                display_user(user_id)

            except ValueError:
                print("Please enter a valid User ID.")


        # ----------------------------------------
        # Option 3
        # ----------------------------------------

        elif choice == "3":

            try:
                user_id = int(input("Enter User ID: "))
                display_usage(user_id)

            except ValueError:
                print("Please enter a valid User ID.")


        # ----------------------------------------
        # Option 4
        # ----------------------------------------

        elif choice == "4":

            try:
                user_id = int(input("Enter User ID: "))

                if user_id in users:
                    display_prediction(user_id)

                else:
                    print("User not found.")

            except ValueError:
                print("Please enter a valid User ID.")


        # ----------------------------------------
        # Option 5
        # ----------------------------------------

        elif choice == "5":

            print("\nApp Categories:")

            for category in sorted(app_categories):
                print("-", category)


        # ----------------------------------------
        # Option 6
        # ----------------------------------------

        elif choice == "6":

            print("\nHigh-Risk Categories:")

            for category in sorted(high_risk_categories):
                print("-", category)


        # ----------------------------------------
        # Option 7
        # ----------------------------------------

        elif choice == "7":

            print("\nThank you for using App Addiction Risk Predictor!")
            break


        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
