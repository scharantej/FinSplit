## Flask Application Design

### Overview

#### Objectives:
- Build a web application to split payments between users by syncing their credit card statements.

#### Approach:
- Design a Flask application with an intuitive user interface and the necessary data processing capabilities.

### HTML Files

#### Login Page (login.html):
- Form for users to sign in or create an account.
- Includes fields for email and password.

#### Payment Sync Page (sync.html):
- Form for users to connect their credit card accounts.
- Includes fields for API keys or OAuth authorization.

#### User Dashboard (dashboard.html):
- Dashboard where users can view their transactions and split payments.
- Includes tables for transactions and payment requests.

### Routes

#### Login Route (/login):
- Verifies user credentials and authenticates the user.
- Redirects to the Payment Sync Page if successful.

#### Payment Sync Route (/sync):
- Connects to the user's credit card provider.
- Retrieves and stores transaction data in the application database.
- Redirects to the User Dashboard.

#### User Dashboard Route (/dashboard):
- Displays the user's transaction and payment request data.
- Provides options for splitting payments and requesting payments from other users.

#### Payment Split Route (/split):
- Allows users to select transactions to split and specify payment details.
- Generates payment requests and sends notifications to the recipients.

#### Payment Request Route (/request):
- Displays payment requests received by the user.
- Allows users to accept or decline requests and make payments.

#### Additional Routes:
- Profile management routes for updating user information.
- Forgot password and account activation routes for account management.
- Error pages for handling exceptions and displaying error messages.