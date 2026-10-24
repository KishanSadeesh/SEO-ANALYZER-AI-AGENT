🤖 SEO Analyzer Agent

An AI-powered SEO analysis agent built with Python, Google's Gemini API, SimplerLLM, and RapidAPI. The project explores how AI agents can interpret user requests, select tools, execute actions, and use the results to answer SEO-related questions.

🚀 About the Project

The SEO Analyzer Agent uses the ReAct (Reasoning and Acting) approach to connect an LLM with external SEO tools.

Instead of simply generating an answer from its training data, the agent can identify an SEO task, call an available action, and use the returned data to help answer the user's question.

This project is part of my journey into AI agent development and practical applications of large language models.

✨ Features

AI-powered agent: Uses Google's Gemini API to interpret user queries.

ReAct architecture: Follows a reasoning-and-action workflow.

SEO data retrieval: Connects to a website SEO analyzer through RapidAPI.

Tool calling: Maps agent-generated actions to Python functions.

Structured output parsing: Extracts JSON-formatted actions from LLM responses.

Python-based implementation: Uses modular Python files for prompts, actions, and agent execution.

🛠️ Tech Stack

Language: Python

LLM: Google Gemini

LLM integration: SimplerLLM

SEO data: RapidAPI website SEO analyzer

HTTP requests: Requests

Version control: Git and GitHub