WHE WHE Cash Register System
Overview
WHE WHE is a simple, React-based cash register interface that lets a cashier pick five unique numbers (1–20), assign dollar values, and finalize a ticket. It uses React state and props to manage data, with no local or session storage.

Features
Number Selection

Display buttons 1–20 in a grid

Highlight or outline a button when selected

Allow up to five selections; unselect by clicking again

Money Assignment

Provide $1, $5, $10, and $20 buttons

Enable only after five numbers are chosen

Add to a running total each time a money button is pressed

Controls

Clear resets both the number picks and the total

Random picks five unique random numbers and resets the total

Cash displays a summary of chosen numbers and total value

State Management

All data lives in React state (useState)

No use of localStorage or sessionStorage

