// src/App.js — Main component for the WHE WHE Cash Register

import React, { useState } from 'react'
import './App.css'
import NumberGrid from './NumberGrid'
import MoneyPad from './MoneyPad'
import SelectedList from './SelectedList'
import Controls from './Controls'

function App() {
  // This array holds up to five numbers the cashier picks
  const [selected, setSelected] = useState([])
  // This number tracks the running total of dollars added
  const [total, setTotal] = useState(0)

  // Flip a number on or off in the selected list, but only up to five picks
  const toggleNumber = (n) => {
    if (selected.includes(n)) {
      // If it was already picked, remove it
      setSelected(selected.filter(x => x !== n))
    } else if (selected.length < 5) {
      // If there’s room, add it to the list
      setSelected([...selected, n])
    } else {
      // Otherwise, warn the cashier they’ve hit the limit
      alert('You can only choose 5 numbers')
    }
  }

  // Only let the cashier add money once five numbers are chosen
  const addMoney = (amt) => {
    if (selected.length < 5) {
      alert('Select 5 numbers first')
    } else {
      // Increase the total by the button’s value
      setTotal(total + amt)
    }
  }

  // Reset everything back to an empty state
  const clearAll = () => {
    setSelected([])
    setTotal(0)
  }

  // Pick five unique random numbers and wipe the total clean
  const pickRandom = () => {
    const pool = Array.from({ length: 20 }, (_, i) => i + 1)
    const picks = []
    while (picks.length < 5) {
      const idx = Math.floor(Math.random() * pool.length)
      picks.push(...pool.splice(idx, 1))
    }
    setSelected(picks)
    setTotal(0)
  }

  // Show a simple pop-up with the final ticket info
  const cashOut = () => {
    alert(
      'Your ticket:\n' +
      'Numbers: ' + selected.join(', ') + '\n' +
      'Total: $' + total
    )
  }

  return (
    <div className="app">
      {/* Left side: number buttons and money pad */}
      <div className="left-panel">
        <NumberGrid selected={selected} onToggle={toggleNumber} />
        <MoneyPad onAdd={addMoney} disabled={selected.length < 5} />
      </div>

      {/* Right side: display picks and action buttons */}
      <div className="right-panel">
        <SelectedList numbers={selected} total={total} />
        <Controls
          onClear={clearAll}
          onRandom={pickRandom}
          onCash={cashOut}
        />
      </div>
    </div>
  )
}

export default App