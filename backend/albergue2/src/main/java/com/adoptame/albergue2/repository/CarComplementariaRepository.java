package com.adoptame.albergue2.repository;

import com.adoptame.albergue2.model.CaracteristicaComplementaria;
import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

@Repository
public interface CarComplementariaRepository extends JpaRepository<CaracteristicaComplementaria, Integer> {
    
}
