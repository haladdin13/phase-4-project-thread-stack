import React, {useState, useEffect} from "react";
import CategoryConteiner from "./CategoryContainer";
import CreateCategory from "./CreateCategory";
import CategoryObject from "./CategoryObject";


function Category(){

    return(
        <div>
            <CategoryConteiner />
            <CreateCategory />
            <CategoryObject />
        </div>
    )
}