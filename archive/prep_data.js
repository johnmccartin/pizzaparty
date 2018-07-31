
var fs = require('fs')
var path = require('path')
var includes = require('array-includes')




function clean_dataset() {
    var root_path = './data/'
    var yelp_json = 'yelp/yelp_academic_dataset_business.json'
    var data = JSON.parse(fs.readFileSync(root_path+yelp_json, 'utf8'))
    var data_clean = []
    

    data.forEach(function(element){
        var business_clean = {}
        var cats = element.categories


        if( includes(cats,"Restaurants") || includes(cats, "Specialty Foods") || includes(cats,"Grocery") ) {

            business_clean.name = element.name

            if ( includes(cats,"Italian") == true || includes(cats,"Pizza") == true ) {
                business_clean.italo_status = "Italian"
            } else {
                business_clean.italo_status = "Not Italian"
            }

            data_clean.push(business_clean)
        }

        
       

    })

    data_clean = JSON.stringify(data_clean)

    fs.writeFileSync(path.join( root_path, "yelp_restaurants_is_italian_pizza.json"), data_clean ,  {encoding: 'utf-8'})



}


clean_dataset()







