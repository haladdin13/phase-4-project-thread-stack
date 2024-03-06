import React, {useState, useEffect} from "react";
import CategoryContainer from "./category_components/CategoryContainer";
import CreateCategory from "./category_components/CreateCategory";


function Category(){

    const [renderCategory, setRenderCategory] = useState([]);

    const addCategory = (newCategory) => {
        console.log(newCategory); // Log the newCategory to verify its structure
        if (newCategory && newCategory.id) { // Ensure newCategory is not undefined and has an id
            setRenderCategory(prevCategories => [...prevCategories, newCategory]);
        } else {
            console.error('Attempted to add an undefined or invalid category:', newCategory);
        }
    };
    

    useEffect(() =>{
        fetch(`http://localhost:5555/categories`).then(res => {
            if (res.status != 200){
                console.log("error")
                return
            }
            res.json().then(data => {
                if (data != null){
                    setRenderCategory(data)
                    console.log(data)
                }
            })
        })
    }, []);

    return(
        <div>
            <CreateCategory onAddCategory={addCategory} />
            <CategoryContainer renderCategory={renderCategory}/>
        </div>
    )
}

export default Category;