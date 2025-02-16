CREATE TABLE public.studentinfo (
    roll_no integer NOT NULL,
    name character varying(50),
    password character varying(50),
    CONSTRAINT studentinfo_pkey PRIMARY KEY (roll_no)
);

CREATE TABLE public.teachersinfo (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    pass character varying(50) NOT NULL,
    CONSTRAINT teachersinfo_pkey PRIMARY KEY (id)
);

CREATE TABLE public.asp (
    roll_no integer,
    dates date,
    status character varying(1) NOT NULL,
    CONSTRAINT unique_attendance3 UNIQUE (roll_no, dates),
    CONSTRAINT asp_roll_no_fkey FOREIGN KEY (roll_no) REFERENCES public.studentinfo(roll_no)
);

CREATE TABLE public.dsc (
    roll_no integer,
    dates date,
    status character varying(1) NOT NULL,
    CONSTRAINT unique_attendance2 UNIQUE (roll_no, dates),
    CONSTRAINT dsc_roll_no_fkey FOREIGN KEY (roll_no) REFERENCES public.studentinfo(roll_no)
);

CREATE TABLE public.java (
    roll_no integer,
    dates date,
    status character varying(1),
    CONSTRAINT unique_attendance0 UNIQUE (roll_no, dates),
    CONSTRAINT fk_roll FOREIGN KEY (roll_no) REFERENCES public.studentinfo(roll_no)
);

CREATE TABLE public.python (
    roll_no integer,
    dates date,
    status character varying(1) NOT NULL,
    CONSTRAINT unique_attendance1 UNIQUE (roll_no, dates),
    CONSTRAINT python_roll_no_fkey FOREIGN KEY (roll_no) REFERENCES public.studentinfo(roll_no)
);

INSERT INTO public.studentinfo (roll_no, name, password) VALUES
(236058, 'SHAIKH ARMAN SALIM', 'Arman'),
(246308, 'PANDHARE SIDDHI ANIL', 'Siddhi'),
(236049, 'PATIL SHREYA SANJAY', 'Shreya'),
(236050, 'POKHALEKAR NEHA VIJAY', NULL),
(236051, 'POTDAR RAJNANDINI MAHENDRA', NULL),
(236052, 'POWAR NISHA BHAGWAN', NULL),
(236053, 'POWAR SHWETA ASHOK', NULL),
(236054, 'POWAR VARAD SANGRAM', NULL),
(236055, 'PURI VAIBHAV DATTA', NULL),
(236056, 'ROTE OMKAR VITTHAL', NULL),
(236057, 'SANGAR SHREYA AMAR', NULL),
(236059, 'SHAIKH HUJAIFA RAFIK', NULL),
(236060, 'SHINDE ANURAG SANGRAM', NULL),
(236061, 'SHINGE PUSHKRAJ PRAMOD', NULL),
(236062, 'SHIRKE ATHARV VIJAY', NULL),
(236063, 'SUTAR KAVITA SHIVAJI', NULL),
(236064, 'SUTAR SUHANI PRADIP', NULL),
(236065, 'TELI SHIVANI SANDIP', NULL),
(236066, 'TIKODE SRUSHTI SANJAY', NULL),
(236067, 'VADAR SHUBHAM PUNDLIK', NULL),
(236068, 'VARUTE PATIL UTKARSHA DIGAMBAR', NULL),
(236069, 'VIBHUTE PRIYANKA PRAKASH', NULL),
(236070, 'VIBHUTE SHRUSHTI UTTAM', NULL),
(236071, 'WAINGADE PRATIKSHA VILAS', NULL),
(246301, 'BANATE VISHWAJIT VASANT', NULL),
(246302, 'BENADE YUVARAJ DATTATRAY', NULL),
(246303, 'GADWE VAISHNAVI DATTA', NULL),
(246304, 'KALE ALOK MANOJ', NULL),
(246305, 'KUDKE YOGESH YUVRAJ', NULL),
(246306, 'MADHALE PRUTHVIRAJ SHAHU', NULL),
(246307, 'NAIK YADNIK VIJAY', NULL),
(246309, 'PATIL POOJA SUDHANRAJ', NULL),
(246310, 'PATIL PRANAV RAJARAM', NULL),
(246311, 'UGILE SUMIT RAJKUMAR', NULL),
(246312, 'PATILOMKAR DINKAR', NULL);
