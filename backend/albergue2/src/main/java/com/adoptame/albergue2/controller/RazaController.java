package com.adoptame.albergue2.controller;

import com.adoptame.albergue2.model.Raza;
import com.adoptame.albergue2.service.RazaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/raza_routes")
public class RazaController {

    @Autowired
    private RazaService razaService;

    @GetMapping("/get_razas")
    public ResponseEntity<Map<String, Object>> getRazas() {
        List<Raza> razas = razaService.obtenerTodasLasRazas();

        if (razas.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "No se encontraron razas.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Razas encontradas.",
            "status", 200,
            "data", razas
        );
        return ResponseEntity.ok(response);
    }

    @PostMapping("/get_raza")
    public ResponseEntity<Map<String, Object>> getRaza(@RequestBody Map<String, Object> payload) {
        if (!payload.containsKey("id_raza")) {
            Map<String, Object> response = Map.of(
                "message", "ID de raza no proporcionado.",
                "status", 400
            );
            return ResponseEntity.badRequest().body(response);
        }

        Integer idRaza = (Integer) payload.get("id_raza");
        Optional<Raza> raza = razaService.obtenerRazaPorId(idRaza);

        if (raza.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "Raza no encontrada.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Raza encontrada.",
            "status", 200,
            "data", raza.get()
        );
        return ResponseEntity.ok(response);
    }
}
