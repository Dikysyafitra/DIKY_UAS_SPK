PGDMP     $    3            
    {            uas    14.9    14.9 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16457    uas    DATABASE     f   CREATE DATABASE uas WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Indonesian_Indonesia.1252';
    DROP DATABASE uas;
                postgres    false            �            1259    16468 
   tbl_leptop    TABLE     l  CREATE TABLE public.tbl_leptop (
    no integer NOT NULL,
    brand character varying(255) NOT NULL,
    ram character varying(255) NOT NULL,
    cpu character varying(255) NOT NULL,
    gpu character varying(255) NOT NULL,
    baterai character varying(255) NOT NULL,
    harga character varying(255) NOT NULL,
    ukuran_layar character varying(255) NOT NULL
);
    DROP TABLE public.tbl_leptop;
       public         heap    postgres    false            �            1259    16467    tbl_leptop_no_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_leptop_no_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.tbl_leptop_no_seq;
       public          postgres    false    210            �           0    0    tbl_leptop_no_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.tbl_leptop_no_seq OWNED BY public.tbl_leptop.no;
          public          postgres    false    209            [           2604    16471    tbl_leptop no    DEFAULT     n   ALTER TABLE ONLY public.tbl_leptop ALTER COLUMN no SET DEFAULT nextval('public.tbl_leptop_no_seq'::regclass);
 <   ALTER TABLE public.tbl_leptop ALTER COLUMN no DROP DEFAULT;
       public          postgres    false    209    210    210            �          0    16468 
   tbl_leptop 
   TABLE DATA           \   COPY public.tbl_leptop (no, brand, ram, cpu, gpu, baterai, harga, ukuran_layar) FROM stdin;
    public          postgres    false    210   [
       �           0    0    tbl_leptop_no_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.tbl_leptop_no_seq', 10, true);
          public          postgres    false    209            �   3  x���KN�0E�/�x���ر����A�)jL�b�QH��)��1`Il�|�J4iQg�M�ν��������mL�/a�mL�WyaЊ�=J'p���6���΋���<F�

�Z<��Rn���h��u8�}��p���O���B�I
��4ItKD�4b��?�+A�(үe��C��m�KS�,NƹQ#����hzY��/*
ZW4W�e��d3�>�xz�F��j�adҴ��%�Cs��T0)�7���ܩU�QC�Z�fWc}b����>B^��v Ix`�u�>7�jR6cx�1��8����     