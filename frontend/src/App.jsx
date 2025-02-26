import { useEffect, useState } from 'react'
import './App.css'
import api from './api'
import Student from './Student'

function App() {
  const [students, setStudents] = useState([])

  const fetchStudents = async () => {
    try {
      const response = await api.get("/")
      const data = response.data.studenti
      setStudents(data)
    } catch (error) {
      console.error("Errore:", error)
    }
  }

  useEffect(() => {
    fetchStudents()
  }, [])

  return (
    <>
      <h1>
        Studenti
      </h1>
      {
        students.length > 0 ? (
          students.map((student, index) => (
            <Student 
              key={index}
              first_name={student.first_name}
              last_name={student.last_name}
              email={student.email}
              age={student.age}
            />
          ))
        ) : (
          <p>Nessuno studente trovato.</p>
        )
      }
    </>
  )
}

export default App
