// MoneyPad.js — displays the dollar-value buttons for adding to the total

import React from 'react'

export default function MoneyPad({ onAdd, disabled }) {
  // These are the bill denominations the cashier can choose
  const values = [1, 5, 10, 20]

  return (
    <div className="money-pad">
      {values.map(v => (
        // Each button shows a dollar amount and triggers onAdd when clicked
        <button
          key={v}
          className="btn"
          disabled={disabled}           // only active once 5 numbers are picked
          onClick={() => onAdd(v)}      // add this value to the running total
        >
          ${v}
        </button>
      ))}
    </div>
  )
}
