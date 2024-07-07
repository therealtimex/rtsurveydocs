---
title: "Connecting to a server"
description: "Learn how to connect the rtSurvey mobile app to your project server, access role-specific functionalities, and start collaborating on surveys across multiple projects."
icon: "cloud_sync"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 313
---

Connecting the rtSurvey app to a server is a crucial step to start using the app for data collection, management, and analysis. This process ensures that all survey roles can access the necessary functionalities and data in real-time.

## Key Differences from ODK Collect

rtSurvey offers enhanced functionalities compared to ODK Collect, catering to various survey roles:
- **Administrator**: Messaging, notifications for updates (data submission, new reports, new accounts), form filling, and viewing analysis reports.
- **Project Manager**: Similar functionalities as Administrators, including project setup and management.
- **Survey Designer**: Messaging, notifications, form filling, and viewing analysis reports.
- **Field Enumerator**: Form filling, messaging, notifications, and progress reports.
- **Data Analyst**: Messaging, notifications, and access to analytics reports.

## Steps to Connect rtSurvey App to a Server

### 1. Ensure You Have an Account

To connect to the server, you need an account. Accounts can be created by an Administrator or by staff using an account creation URL set up by the Administrator.

### 2. Open rtSurvey App

Launch the rtSurvey app on your mobile device. If you haven't installed it yet, refer to the [Installing rtSurvey App](#installing-rtsurvey-app) page.

### 3. Access the Server Connection Settings

1. Open the app and navigate to the settings menu.
2. Select the option to connect to a server.

### 4. Enter Account Details and Select Project

When connecting to rtSurvey, the process is streamlined based on your account configuration:

- **Username**: Enter your account username.
- **Password**: Enter your account password.

After entering your credentials:

- If your account is associated with only one survey project:
  - The app will automatically sign you into that project's server.
  - You don't need to enter a server URL or select a project manually.

- If your account is associated with multiple survey projects:
  - After successful authentication, you'll see a list of projects you have access to.
  - Select the project you want to work on from this list.

### 5. Authenticate

After entering the server details, tap on the "Connect" or "Login" button. The app will authenticate your credentials and establish a connection to the server.

```mermaid
flowchart TD
    A["📱 Start rtSurvey App"] --> B["🔑 Enter Username<br>and Password"]
    style A fill:#4CAF50,stroke:#666666,stroke-width:3px,color:white
    style B fill:#2196F3,stroke:#666666,stroke-width:3px,color:white

    B --> C{"🌳 Multiple<br>projects?"}
    style C fill:#FFC107,stroke:#666666,stroke-width:3px,color:black

    C -->|Yes| D["📋 Display list<br>of projects"]
    C -->|No| E["🔄 Auto-connect to<br>single project"]
    style D fill:#FF9800,stroke:#666666,stroke-width:3px,color:white
    style E fill:#009688,stroke:#666666,stroke-width:3px,color:white

    D --> F["👆 User selects<br>a project"]
    style F fill:#FF5722,stroke:#666666,stroke-width:3px,color:white

    E --> G["☁️ Connect to server"]
    F --> G
    style G fill:#3F51B5,stroke:#666666,stroke-width:3px,color:white
    G --> H["👥 Access role-specific<br>functionalities"]
    style H fill:#9C27B0,stroke:#666666,stroke-width:3px,color:white

    H --> I["👨‍💼 Administrator/<br>Project Manager"]
    H --> J["🎨 Survey Designer"]
    H --> K["📝 Field Enumerator"]
    H --> L["📊 Data Analyst"]
    style I fill:#E91E63,stroke:#666666,stroke-width:3px,color:white
    style J fill:#795548,stroke:#666666,stroke-width:3px,color:white
    style K fill:#607D8B,stroke:#666666,stroke-width:3px,color:white
    style L fill:#8BC34A,stroke:#666666,stroke-width:3px,color:white

    I --> M["💬 Messaging<br>🔔 Notifications<br>📄 Form Filling<br>📈 Viewing Reports"]
    J --> N["💬 Messaging<br>🔔 Notifications<br>🧪 Form Testing<br>📈 Viewing Reports"]
    K --> O["📝 Form Filling<br>💬 Messaging<br>🔔 Notifications<br>📊 Progress Reports"]
    L --> P["💬 Messaging<br>🔔 Notifications<br>📊 Analytics Reports"]
    style M fill:#FF4081,stroke:#666666,stroke-width:3px,color:white
    style N fill:#9E9E9E,stroke:#666666,stroke-width:3px,color:white
    style O fill:#00BCD4,stroke:#666666,stroke-width:3px,color:white
    style P fill:#CDDC39,stroke:#666666,stroke-width:3px,color:white
```

## Troubleshooting Connection Issues

If you encounter issues while connecting to the server:

1. **Check Internet Connection**: Ensure your device is connected to the internet.
2. **Confirm Credentials**: Ensure your username and password are correct.
3. **Restart the App**: Close and reopen the rtSurvey app.
4. **Contact Support**: If issues persist, contact your system administrator or rtSurvey support for assistance.

## Conclusion

Connecting the rtSurvey app to a server is a straightforward process that enables you to leverage the full capabilities of the app. By following the steps outlined above, you can ensure seamless data collection, management, and analysis tailored to your specific survey role.
