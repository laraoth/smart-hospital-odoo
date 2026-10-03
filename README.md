# Smart Hospital Odoo

A hospital management system developed using Odoo 17, PostgreSQL, and Docker.

## Overview

Smart Hospital is a customized Odoo-based hospital management project designed to support healthcare-related workflows, including medical staff recruitment, patient triage, and IoT-based vital-sign alerts.

## Technologies

- Odoo 17
- PostgreSQL 15
- Docker
- Docker Compose
- Python
- XML
- Git / GitHub
- REST-style JSON API

## Custom Odoo Modules

### smart_hospital_core

Extends Odoo functionality with medical staff licensing information, including:

- Medical License Number
- License Expiry Date

These fields are integrated into the Odoo recruitment workflow.

### smart_hospital_pulse

Adds patient vital-sign monitoring functionality to CRM leads.

Features include:

- Patient heart-rate tracking
- Critical heart-rate detection
- Automatic priority update for critical alerts
- Chatter notification for critical vital-sign events
- JSON endpoint for updating patient heart rate

## IoT Integration

The project includes a JSON API endpoint for updating patient heart-rate information:

`/api/hospital/vitals/update`

The endpoint receives a patient/ticket identifier and heart-rate value, then updates the corresponding CRM record.

## Project Structure

```text
smart-hospital-odoo/
│
├── Odoo/
│   ├── smart_hospital_core/
│   └── smart_hospital_pulse/
│
├── docker-compose.yml
├── .gitignore
└── README.md
