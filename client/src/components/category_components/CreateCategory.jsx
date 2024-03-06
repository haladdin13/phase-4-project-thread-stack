import React from 'react';
import { Formik, Form, useField } from 'formik';
import ReactDOM from 'react-dom';
import * as Yup from 'yup';

function CreateCategory(){
    
    const CategoryTextInput = ({ label, ...props }) => {
        const [field, meta] = useField(props);
        return (
            <div className="form-group">
                <label htmlFor={props.id || props.name}>{label}</label>
                <input className='text-input' {...field} {...props} />
                {meta.touched && meta.error ? (
                    <div className="error">{meta.error}</div>
                ) : null}
            </div>
        );
    }
    
    const CategorySelect = ({ label, ...props }) => {
        const [field, meta] = useField(props);
        return (
            <div className="form-group">
                <label htmlFor={props.id || props.name}>{label}</label>
                <select {...field} {...props} />
                {meta.touched && meta.error? (
                    <div className="error">{meta.error}</div>
                ) : null}
            </div>
        );
    }

    const CreateCategoryForm = () => {
        return (
            <Formik
                initialValues={{
                    name: '',
                    description: '',
                }}
                validationSchema={Yup.object({
                    name: Yup.string()
                    .min(3, 'Name must be at least 3 characters long')
                    .required('Name is required'),
                    description: Yup.string()
                    .min(6, 'Description must be at least 6 characters long')
                    .required('Description is required'),
                })}
                onSubmit={(values, { setSubmitting }) => {
                    setTimeout(() => {
                        alert(JSON.stringify(values, null, 2));
                        setSubmitting(false);
                    }, 400);
                }}
        
        >
            <Form>
                <CategoryTextInput label="Name" name="name" />
                <CategoryTextInput label="Description" name="description" />
                <button type="submit">Submit</button>
            </Form>

            </Formik>
            )
            
    }
}

export default CreateCategory;