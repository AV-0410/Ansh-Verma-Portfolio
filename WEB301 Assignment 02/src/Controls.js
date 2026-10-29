//Controls.js — action buttons for clearing, randomizing, and cashing out

import React from 'react'

export default function Controls({ onClear, onRandom, onCash }) {
  return (
    <div className="controls">
      {/* Wipe out all selections and reset the total */}
      <button className="btn" onClick={onClear}>
        Clear
      </button>

      {/* Let the app pick five random numbers and reset money */}
      <button className="btn" onClick={onRandom}>
        Random
      </button>

      {/* Show your final ticket details in a pop-up */}
      <button className="btn" onClick={onCash}>
        Cash
      </button>
    </div>
  )
}