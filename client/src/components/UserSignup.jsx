import React from 'react';
import { Formik, Form, useField } from 'formik';
import * as Yup from 'yup';
import { useNavigate } from 'react-router-dom';
import './SignupStyles.css';



function UserSignup(){
    const navigate = useNavigate()

    const SignupTextInput = ({label, ...props}) => {

        const [field, meta] = useField(props)
        return(
            <div className='form-group'>
                <label htmlFor={props.id || props.name}>{label}</label>
                <input className='text-input' {...field} {...props} />
                {meta.touched && meta.error ? (
                    <div className='error'>{meta.error}</div>
                ) : null}
            </div>
        )
    }

    return(
        <div className='signup-heading'>
            <h1>Signup</h1>
            <div> 
                <Formik
                    initialValues={{
                        user_name: "",
                        email: "",
                        password: ""
                    }}
                    validationSchema={Yup.object({
                        user_name: Yup.string()
                        .required('Username is required.'),
                        email: Yup.string()
                        .required('Email is required.'),
                        password: Yup.string()
                        .required('Password is required')
                    })}
                    onSubmit={(values, { setSubitting, resetForm }) => {

                        fetch(`http://localhost:5555/signup`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify(values)    
                        })
                        .then(res => res.json())
                        .then(values => {
                            console.log(values)
                            navigate('/login')
                        })
                        .then( setSubitting(false), resetForm() );
                    }}
                    >
                        <Form className='SubmitForm'>
                            <SignupTextInput type="text" name="user_name" label="Username" />
                            <SignupTextInput type="email" name="email" label="Email" />
                            <SignupTextInput type="password" name="password" label="Password" />
                            <button type="submit">Submit</button>
                        </Form>
                </Formik>
            </div>
        </div>
    )

}

export default UserSignup;