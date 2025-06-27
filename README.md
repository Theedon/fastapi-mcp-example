# mcp-example

A FastAPI-based MCP (Model Context Protocol) server providing tools for Google Tasks, Google Calendar, and basic calculator operations.

## Features

- **Google Tasks API**: Create and delete tasks using your Google account.
- **Google Calendar API**: Update events in your Google Calendar.
- **Calculator**: Simple math operations (add, subtract).

## Requirements

- Python 3.12+
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

```bash
poetry install
```

## Running the Server

```bash
poetry run uvicorn src.main:app --reload
```

## API Endpoints

- `/calc/add_numbers` (POST): Add two numbers.
- `/calc/subtract_numbers/{a}/{b}` (GET): Subtract two numbers.
- `/google_tasks/create` (POST): Create a Google Task.
- `/google_tasks/delete` (POST): Delete a Google Task.
- `/google_calendar/update_event` (POST): Update a Google Calendar event.
- `/status` (GET): Health check.
- `/metadata` (GET): Server metadata.

## Authentication

Google endpoints require an OAuth2 access token. See the relevant schema files for details.
