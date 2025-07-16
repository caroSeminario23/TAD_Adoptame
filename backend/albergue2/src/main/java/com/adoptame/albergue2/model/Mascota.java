package com.adoptame.albergue2.model;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.OffsetDateTime;

@Entity
@Table(name = "MASCOTA")
public class Mascota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID_MASCOTA", nullable = false)
    private Integer idMascota;

    @Column(name = "NOMBRE", nullable = false, unique = true, length = 15)
    private String nombre;

    @Column(name = "FOTO", nullable = false, columnDefinition = "text")
    private String foto;

    @Column(name = "FEC_NACIMIENTO", nullable = false)
    private java.sql.Date fecNacimiento;

    @Column(name = "SEXO", nullable = false, length = 1)
    private String sexo;

    @Column(name = "ESTATURA", nullable = false, precision = 3, scale = 2)
    private BigDecimal estatura;

    @Column(name = "PESO", nullable = false, precision = 5, scale = 2)
    private BigDecimal peso;

    @ManyToOne
    @JoinColumn(name = "ID_TIPO_MASCOTA", nullable = false)
    private TipoMascota tipoMascota;

    @ManyToOne
    @JoinColumn(name = "ID_RAZA", nullable = false)
    private Raza raza;

    @Column(name = "FEC_INGRESO", nullable = false)
    private OffsetDateTime fecIngreso;

    @Column(name = "ADOPTADO", nullable = false)
    private Boolean adoptado;

    @Column(name = "DISCAPACIDAD", nullable = false)
    private Boolean discapacidad;

    // Constructor vacío (necesario para JPA)
    public Mascota() {
    }

    // Constructor con parámetros
    public Mascota(String nombre, 
                String foto, 
                java.sql.Date fecNacimiento, 
                String sexo,
                BigDecimal estatura, 
                BigDecimal peso, 
                TipoMascota tipoMascota, 
                Raza raza,
                OffsetDateTime fecIngreso, 
                Boolean adoptado, 
                Boolean discapacidad) {
        this.nombre = nombre;
        this.foto = foto;
        this.fecNacimiento = fecNacimiento;
        this.sexo = sexo;
        this.estatura = estatura;
        this.peso = peso;
        this.tipoMascota = tipoMascota;
        this.raza = raza;
        this.fecIngreso = fecIngreso;
        this.adoptado = adoptado;
        this.discapacidad = discapacidad;
    }

    // Getters y setters
    public Integer getIdMascota() {
        return idMascota;
    }

    public void setIdMascota(Integer idMascota) {
        this.idMascota = idMascota;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }

    public java.sql.Date getFecNacimiento() {
        return fecNacimiento;
    }

    public void setFecNacimiento(java.sql.Date fecNacimiento) {
        this.fecNacimiento = fecNacimiento;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public BigDecimal getEstatura() {
        return estatura;
    }

    public void setEstatura(BigDecimal estatura) {
        this.estatura = estatura;
    }

    public BigDecimal getPeso() {
        return peso;
    }

    public void setPeso(BigDecimal peso) {
        this.peso = peso;
    }

    public TipoMascota getTipoMascota() {
        return tipoMascota;
    }

    public void setTipoMascota(TipoMascota tipoMascota) {
        this.tipoMascota = tipoMascota;
    }

    public Raza getRaza() {
        return raza;
    }

    public void setRaza(Raza raza) {
        this.raza = raza;
    }

    public OffsetDateTime getFecIngreso() {
        return fecIngreso;
    }

    public void setFecIngreso(OffsetDateTime fecIngreso) {
        this.fecIngreso = fecIngreso;
    }

    public Boolean getAdoptado() {
        return adoptado;
    }

    public void setAdoptado(Boolean adoptado) {
        this.adoptado = adoptado;
    }

    public Boolean getDiscapacidad() {
        return discapacidad;
    }

    public void setDiscapacidad(Boolean discapacidad) {
        this.discapacidad = discapacidad;
    }
}
