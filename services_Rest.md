#### Services REST à mettre en place

- liste installation selon ville  


      SELECT * FROM INSTALLATION  
      WHERE VILLE = ville
- liste installation selon une activité 


      SELECT * FROM INSTALLATION  
      WHERE NUMERO = (    
      SELECT NUMERO_INSTALLATION, NUMERO  
        FROM EQUIPEMENT  
        WHERE NUMERO = (  
	  SELECT *  
	  FROM EQUIPEMENT_ACTIVITE  
	  WHERE NUMERO_ACTIVITE = activite  
        )  
      )  
- suggestion* de ville
- suggestion* d'activité  

*(suggestion -> completion dans champ recherche)

**plan:**
- requete SQL pour executer ces services
- code python qui utilise les requetes
- :test:
- appli web qui utilise le code en python
