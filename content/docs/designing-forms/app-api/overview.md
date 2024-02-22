---
title: "App API overview"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

The AppAPI allows users to load data from the app using different methods in the FormEngine and DMView. It provides access to various data keys for retrieving specific information from the app.

### Usage

To load data from the app, you can use the following methods:

#### FormEngine (FE)

In the FormEngine, you can use the `pulldata()` function with the following syntax:

calculate | any_name | pulldata('app-api', 'data-key')


- `'app-api'`: This keyword informs the FormEngine to load the data from the app API.
- `'data-key'`: This is the key of the data you want to load from the app API.
  - If the data key is invalid or not supported, the calculation will return "n/a".

#### DMView

In the DMView, you can use the `##data-key##` placeholder to load the data from the app API.

- `'data-key'`: This is the key of the data you want to load from the app API.
  - If the data key is invalid or not supported, the calculation will return an empty text ("").

### Supported Data Keys

Here are the supported data keys that you can use with the AppAPI:

#### key: osPlatform
- Description: Returns the current OS name (Android or iOS) and the OS version. Web platforms will return an empty value.

#### key: appPlatform
- Description: Returns the app platform name. Possible values are:
  - CPMSA (rtWork app)
  - rtSurvey (rtSurvey app)
  - rtHome (rtHome app)

#### key: appVersion
- Description: Returns the app's version name.

#### key: getDisplayWidth
- Description: Returns the device screen width in pixels.

#### key: getDisplayHeight
- Description: Returns the device screen height in pixels.

#### key: getScreenSize
- Description: Returns the device screen size in inches.

#### key: projectCode
- Description: Returns the current project code of the site the user is signing in to.

#### key: projectURL
- Description: Returns the current project URL of the site the user is signing in to. The default/fallback value is an empty text ("").

#### key: startingPoint
- Description: Returns the path of the point that starts the form. Refer to the "Form starting point" for more details.

#### key: serverTime
- Description: Returns the best available approximation of the date and time on the server.

#### key: user.[attribute]
- Description: Returns the current user attributes based on the specified attribute key. Refer to the "User attributes" table for available attribute keys.

#### key: module.[attribute]
- Description: Returns the module attribute of the module that starts the form. Refer to the "Module attributes" table for available attribute keys.

#### key: instancePath
- Description: Returns the current instance folder path.

#### key: appLanguage
- Description: Returns the current app language set in the app's settings (e.g., vi, en).

#### key: openArgs.[attribute]
- Description: Returns the open-form-argument passed from the ActionButton (act_fill_form, act_get_instance). The default/fallback value is an empty text ("").

#### key: primaryAppColor
- Description: Retrieves the app's primary color. For more details, refer to [this link](https://rtgit.rta.vn/rtlab/tech-document/-/blob/main/app-ui/app-primary-color.md).

### User Attributes

Combine the below attribute keys with "user." in the `pulldata()` params to retrieve the current user information. For example, use `user.username`, `user.email`, etc.

| Attribute Key        | Description                          |
|----------------------|--------------------------------------|
| username             | Username of the user                  |
| name                 | Full name of the user                 |
| staffCode            | User's staff code                     |
| phone                | Phone number of the user              |
| email                | Email address of the user             |
| description          | Description text in user information  |
| organization_id      | Organization ID the user belongs to    |
| organization_name    | Organization name the user belongs to  |
| team_id              | Team ID the user belongs to            |
| supervisor_id        | ID of the user's supervisor            |
| user_role            | User role                             |
| user_group           | User group                            |
| is_supervisor        | 1 if the user is a supervisor, 0 if not|
| auto_approve_edit_request | 1 if the user is allowed to approve automatic "request to edit", 0 if not |
| ipcall.user          | IP Call account's parameter - username |
| ipcall.token         | IP Call account's parameter - token    |
| ipcall.password      | IP Call account's parameter - password |
| ipcall.url           | IP Call account'sparam - URL |
| ipcall.auth          | IP Call account's parameter - auth (optional) |
| ipcall.port          | IP Call account's parameter - port (optional) |

### Module Attributes

Combine the below attribute keys with "module." in the `pulldata()` params to retrieve the current module information. For example, use `module.code`, `module.title`, etc.

| Attribute Key        | Description                          |
|----------------------|--------------------------------------|
| code                 | Module code                          |
| version              | Module version                       |
| title                | Module title                         |
| description          | Module description                   |
| subModule.code       | Submodule code                       |
| subModule.title      | Submodule title                      |
| subModule.description| Submodule description                |
| component.code       | Component code                       |
| component.name       | Component name (title)               |
| object.code          | Object code                          |
| object.title         | Object title                         |

### Form Starting Point

The form starting point refers to the path that opens a blank form (create a new instance).

- From action button: `action:parent-id/action-id`
- From module object: `module:module-code/submodule-code/component-code/object-code`
- From another form: `form:family-id/form-id/version`
- From form list: `normal`
