#### Services REST à mettre en place

- la liste des installations d'une ville  


      SELECT * FROM INSTALLATION  
      WHERE VILLE = ville
- la liste des installations d'un numero d'activité


      SELECT *  
      FROM INSTALLATION i1,
      (SELECT NUMERO_INSTALLATION, NUMERO  
        FROM EQUIPEMENT e1,
        (SELECT *  
          FROM EQUIPEMENT_ACTIVITE  
          WHERE NUMERO_ACTIVITE = numero_activite  
        ) e2
        WHERE e1.NUMERO = e2.NUMERO_EQUIPEMENT
      ) i2
      WHERE i1.NUMERO = i2.NUMERO
- suggestion* de ville
- suggestion* d'activité  

*(suggestion -> completion dans champ recherche)
