# CountryInfo_API
This is an API wrapper through which users should be able to get information about specific country.<br/>
Consumers of the API should send HTTP request with the country name and the information they desire. The API should get all the information about the given country from a public [RESTCountries API](https://restcountries.eu/), parse it and respond with the requested information.

## Testing 
The API is covered by both [**unit tests**](https://github.com/BouSenna/CountryInfo_API/tree/master/API_Testing) and [**integration tests**](https://github.com/BouSenna/CountryInfo_API/tree/master/API_IntegrationTesting).<br/>
A [**dummy API**](https://github.com/BouSenna/CountryInfo_API/tree/master/Dummy_API) is provided to be able to run these tests locally without the need of an internet connection or any external resources
<br/><br/>

## API Endpoints
Below are some of the REST endpoints that could be used to search for information about a country.


### All
Request all information about a country.<br/>
  ``` 
  http://localhost:5000/{country_name}
  ```

### Name
Request a country name.<br/>
  ``` 
  http://localhost:5000/{country_name}?info=name  
  ```

### Top Level Domain
Request a country’s top level domain.<br/>
  ``` 
  http://localhost:5000/{country_name}?info=topLevelDomain 
  ```

 
### Codes
##### Alpha 2-Code
Request a country’s alpha 2-code.<br/>
  ```
  http://localhost:5000/{country_name}?info=alpha2Code 
  ``` 
##### Alpha 3-Code
Request a country’s alpha 3-code.<br/> 
  ```
  http://localhost:5000/{country_name}?info=alpha3Code
  ``` 
##### Calling Code
Request a country’s calling code.<br/>
  ``` 
  http://localhost:5000/{country_name}?info=callingCodes
  ``` 

### Capital
Request a country’s capital.<br/>
   ``` 
   http://localhost:5000/{country_name}?info=capital 
   ```

### Region
##### Country Region
Request a country’s region.<br/> 
  ```
  http://localhost:5000/{country_name}?info=region
  ```
##### Country Sub-Region
Request a country’s sub-region.<br/> 
  ``` 
  http://localhost:5000/{country_name}?info=subregion
  ``` 

### Population
Request the population of a country.<br/>
  ```
  http://localhost:5000/{country_name}?info=population
  ```

### Languages
Request the spoken languages in a country.<br/>
  ``` 
  http://localhost:5000/{country_name}?info=languages
  ```

<br/><br/><br/>
## TBC
