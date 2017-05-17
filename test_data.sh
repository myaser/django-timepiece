#!/usr/bin/env bash

python example_project/manage.py loadtestdata --verbosity=3 --traceback --generate-fk=ALL \
        auth.User:3\
        \
        entries.Activity:3 \
        entries.Activity:3 \
        entries.ActivityGroup:3 \
        entries.Location:3 \
        entries.Entry:3 \
        entries.ProjectHours:3 \
        \
        crm.UserProfile:3 \
        crm.Attribute:3 \
        crm.Business:3 \
        crm.Project:3 \
        crm.RelationshipType:3 \
        crm.ProjectRelationship:3 \
        \
        contracts.ProjectContract:3\
        contracts.ContractHour:3\
        contracts.ContractAssignment:3\
        contracts.HourGroup:3\
        contracts.EntryGroup:3

