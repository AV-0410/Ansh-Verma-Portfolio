// SelectedList.js — shows the picked numbers and the running total

import React from 'react'

export default function SelectedList({ numbers, total }) {
  // Keep the numbers in order so they always look tidy
  const sorted = [...numbers].sort((a, b) => a - b);

  return (
    <div className="selected-list">
      {/* Section title */}
      <h3>Numbers Selected</h3>

      {/* Each number turns into its own little badge */}
      <ul>
        {sorted.map(n => (
          <li key={n}>{n}</li>
        ))}
      </ul>

      {/* Show the current dollar total right below */}
      <p>Total: ${total}</p>
    </div>
  )
}