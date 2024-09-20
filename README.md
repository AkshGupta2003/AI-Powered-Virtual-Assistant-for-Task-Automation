# AI-Powered-Virtual-Assistant-for-Task-Automation

## Description

This project implements a multi-agent system for scheduling meetings and sending emails using Google Calendar and Gmail APIs. It leverages large language models (LLMs) for natural language processing and task automation.

## Key Features

- Meeting Scheduling: Proposes, schedules, and manages meetings using the Google Calendar API.
- Email Drafting: Collaboratively drafts email responses using LLMs.
- Automated Communication: Sends emails through the Gmail API based on user requests.
- Multi-Agent Collaboration: Leverages UserProxy, Planner, Emailer, and Critic agents for efficient task execution.

## Installation

### Prerequisites:

- Python 3.x
- autogen library (Install using pip install autogen)
- Google Cloud Platform project with enabled Calendar and Gmail APIs (See https://developers.google.com/calendar/api/quickstart/js)
- Download credentials JSON files for Calendar and Gmail API access (Follow instructions at the link above)

### Place credential files:

Place the downloaded JSON credentials files (credentials.json and token.json) in a suitable location (e.g., project directory). Ensure proper access permissions.

## Usage

The project simulates a user interaction to initiate meeting scheduling and email communication. You can replace the example message with your desired meeting details:

Schedule a meet with ABC(ABC@gmail.com) on 16-09-2024 at 12PM for half an hour. Send a mail on my behalf asking him to join on time.

## Components

- calendar_service.py: Provides functions for adding, updating, and deleting events from Google Calendar.
- gmail_service.py: Offers functionalities for sending emails through the Gmail API.
- app.ipynb: The entry point for the project, initializing agents, registering functions, and starting the chat simulation.

## Screenshots
<p align="center">
    <img src="https://github.com/AkshGupta2003/AI-Powered-Virtual-Assistant-for-Task-Automation/blob/main/Screenshot/event%20.png">
    &nbsp;
    <img src="https://github.com/AkshGupta2003/AI-Powered-Virtual-Assistant-for-Task-Automation/blob/main/Screenshot/mail.png">
</p>
