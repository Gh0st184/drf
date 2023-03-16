import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';


const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className='table table-striped mx-auto w-auto' style={{'width': '50%'}}>
            <th scope='col' style={{'width': '25%'}}>
                First name
            </th>
            <th scope='col' style={{'width': '25%'}}>
                Last name
            </th>
            <th scope='col' style={{'width': '25%'}}>
                Email
            </th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UserList;
