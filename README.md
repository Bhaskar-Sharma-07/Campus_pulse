# ⚡ Campus Pulse — AI Notice Organizer for College Hackathons

> **Solving Student Notice Overload, Missed Deadlines & WhatsApp Group Spam with Intelligent Entity Extraction and Executive Summaries.**

![Campus Pulse UI Preview](https://img.shields.io/badge/Status-Hackathon%20Ready-emerald?style=for-the-badge&logo=react)
![Tailwind CSS](https://img.shields.io/badge/Style-Dark%20Glassmorphism-cyan?style=for-the-badge&logo=tailwindcss)
![AI Powered](https://img.shields.io/badge/AI-NLP%20Notice%20Parser-purple?style=for-the-badge)

---

## 📌 The Problem
College students are inundated with hundreds of unstructured messages every week across dozens of official and unofficial WhatsApp groups, Telegram channels, and email blasts. Critical assignment deadlines get lost in chit-chat, exam reschedule notices are overlooked, and hackathon registrations expire without students noticing.

## 🚀 The Solution: Campus Pulse
**Campus Pulse** transforms chaotic text forwards into a centralized, beautifully organized, and actionable intelligence feed. It bridges the gap between chaotic group chats and structured task management.

---

## ✨ Core Features

### 1. 🤖 Smart Input (AI Notice Parser)
- **Unstructured Text Extraction**: Simply paste forwarded WhatsApp text, raw faculty emails, or flyer captions.
- **Automated Entity Recognition**: Automatically extracts:
  - **Title**: Clean synthesized headline stripping noisy emojis and repetitive warnings.
  - **Date & Time**: Resolves absolute dates (*"Nov 5"*) and relative terms (*"tonight"*, *"tomorrow"*, *"this Friday"*) anchored to today's date (`Oct 31, 2026`).
  - **Venue & Location**: Detects physical halls, labs, auditoriums, or digital platforms (e.g., *Google Classroom*, *SBI Collect*).
  - **Category**: Classifies automatically into `Academic`, `Event`, `Deadline`, `Club`, or `General`.
  - **Urgency Level**: Assesses priority into `Urgent`, `Medium`, or `Low` based on deadline proximity and critical keywords.
  - **Action Checklist**: Identifies immediate prerequisites (e.g. *bring hall ticket*, *register 4-person team*).
- **1-Tap Judge Samples**: Instant sample buttons (*Assignment Deadline Tonight*, *HackTech Hackathon*, *Math Exam Rescheduled*, *Drama Auditions*, *Semester Fee Extension*) plus an **"Instant 1-Click Parse"** button for immediate evaluation.

### 2. 📋 Organised Feed & Visual Calendar
- **Dynamic List View**:
  - Dark glassmorphism cards with category-specific glowing neon borders.
  - Priority status pills (`Due Today`, `Tomorrow`, `Upcoming in X days`, `Expired`).
  - Collapsible original message drawer to cross-reference the original WhatsApp forward anytime.
  - Quick actions: Mark Done/Completed, Download `.ICS` Calendar file, Copy Clean Summary, or Delete.
- **Visual Month Calendar View**:
  - Full interactive calendar grid with glowing color-coded event chips.
  - Interactive day agenda drawer displaying all events and deadlines for any selected date.
- **Search & Multi-Filtering**:
  - Live full-text search across titles, venues, and descriptions.
  - Category tabs with real-time notice counters (`Academic`, `Event`, `Deadline`, `Club`, `General`).
  - Status filters (`🔥 Today`, `⏳ Upcoming`, `🚨 Urgent`).
  - Multi-criteria sorting (Earliest Date, Latest Date, Urgency First, Recently Added).

### 3. 🚨 Priority & Attention Today Hero Section
- Automatic detection of any notices requiring immediate action today (`Oct 31, 2026`).
- Dedicated pulsating emergency banner highlighting closing deadlines, venue locations, and quick resolution buttons.

### 4. ⚡ "What do I need to know this week?" (AI Weekly Digest)
- High-impact executive summary modal accessible from the top navigation bar.
- Synthesizes all active notices into a readable briefing:
  - **Immediate Action Items** (deadlines closing within 48 hours).
  - **Academic & Exam Schedule**.
  - **Campus Events & Club Opportunities**.
- **1-Click WhatsApp Export**: Formats the briefing with emojis and clean indentation ready to be copied and forwarded directly back into student groups.

### 5. 🎯 Usability, Storage & Polish
- **Sleek Dark / Light Mode**: Default high-end dark glassmorphism theme with instant 1-click toggle to a clean, high-contrast light theme (persisted via `localStorage`).
- **Zero Onboarding**: Designed for first-time users with intuitive touch targets.
- **Persistent LocalStorage**: All added notices and edits persist across browser refreshes.
- **Calendar Integration**: Export any notice as an `.ICS` calendar file compatible with Google Calendar, Apple Calendar, and Outlook.
- **Audio Feedback**: Subtle Web Audio API synth chimes on extraction and task completion (with mute toggle).
- **Judge Reset Button**: Easily restore the preloaded demo dataset with 1 click.

---

## 🛠️ Tech Stack
- **Framework**: React 18 (SPA Architecture)
- **Styling**: Tailwind CSS with custom Glassmorphism aesthetics, dark palette (`#060911`), and neon glow effects
- **Icons**: Crisp SVG Lucide-compatible icon system
- **Effects**: HTML5 Canvas Confetti & Web Audio API synthesizer
- **Persistence**: Browser `localStorage` API

---

## 🏃 Quick Start (How to Run)

### Option 1: Double-Click (Zero Setup)
Simply open `index.html` in any modern web browser (Google Chrome, Microsoft Edge, Brave, Firefox, or Safari).

### Option 2: Local Server via Python
Run the included python server which automatically opens your browser:
```bash
python server.py
```
Or on Windows:
```bash
run.bat
```
Navigate to: [http://localhost:5173](http://localhost:5173)

---

## 🧪 Hackathon Judging Walkthrough

1. **Test the AI Parser**:
   - In the **Smart Input** section, click on any of the sample pills (e.g. `🚨 Project Deadline (Urgent)` or `🚀 HackTech 2026 Hackathon`).
   - Click **"Extract with AI"** (or use the **"Instant 1-Click Parse"** button).
   - Watch the animated AI step recognition scan the text and present the structured card with high confidence.
   - Click **"Confirm & Add Notice Card"** to save it to your pulse board.

2. **Inspect the Attention Today Banner**:
   - Notice the glowing red emergency banner at the top for the Capstone Project Deadline due tonight.
   - Click **"Mark Done"** or **"Sync Calendar"**.

3. **Explore List & Calendar Views**:
   - Filter by categories: `Deadline`, `Event`, `Academic`, `Club`.
   - Switch between **List View** and **Calendar View** to see the interactive month grid and day agenda.

4. **Generate the Weekly Digest**:
   - Click the glowing gradient button **"What do I need to know this week?"** in the top header.
   - Review the categorized executive briefing and click **"Copy WhatsApp Digest"**.

5. **Reset Anytime**:
   - Click the 🔄 refresh icon in the header or footer to reset back to the default demo data at any time.

---

*Built with passion for students & hackathons.*
