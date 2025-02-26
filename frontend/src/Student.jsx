import './Student.css'

const Student = ({ first_name, last_name, age, email }) => {
    return (
        <div className="studentDiv">
            <div>{ first_name }</div>
            <div>{ last_name }</div>
            <div>{ age }</div>
            <div>{ email }</div>
        </div>
    )
}   

export default Student