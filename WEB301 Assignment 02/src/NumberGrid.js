// NumberGrid.js — renders the 1–20 buttons and handles selection toggles

import React from 'react'

export default function NumberGrid({ selected, onToggle }) {
  return (
    <div className="grid">
      {Array.from({ length: 20 }, (_, i) => i + 1).map(n => (
        // For each number, show a button
        <button
          key={n}
          // If this number is in the selected list, highlight it
          className={selected.includes(n) ? 'btn selected' : 'btn'}
          // When clicked, tell the parent to toggle this number
          onClick={() => onToggle(n)}
        >
          {n}
        </button>
      ))}
    </div>
  )
}
