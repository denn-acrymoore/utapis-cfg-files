import unittest
from cfg_initialization import cfg_true_or_false


class TestKonjSubor(unittest.TestCase):
    def test_konj_sub_tnp_koma_1_kata_awal_klausa_01(self):
        """
        -> Kj Sub Tnp Koma 1 Kata Awal Klausa 01
        (Karena, kj_sub_tnp_koma_kt_pertama), (bekerja, verba),
        (asal-asalan, adjektiva), (,, td_koma), (Jeje, nomina),
        (tidak, tidak), (mendapatkan, verba), (bonus, nomina),
        (gaji, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_tnp_koma_kt_pertama>",
            "<verba>",
            "<adjektiva>",
            "<td_koma>",
            "<nomina>",
            "<tidak>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_tnp_koma_1_kata_awal_klausa_02(self):
        """
        -> Kj Sub Tnp Koma 1 Kata Awal Klausa 02
        (Jika, kj_sub_tnp_koma_kt_pertama), (Anda, nomina), (mau, adverbia),
        (mendengarkannya, verba), (,, td_koma), (saya, nomina), (tentu, adjektiva),
        (senang, adjektiva), (sekali, adverbia), (menceritakannya, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<adjektiva>",
            "<adjektiva>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_tnp_koma_1_kata_akhir_klausa_01(self):
        """
        -> S-P-F_KJ_SUB ([N-PUN]-[ADV-V-V]-[KJ_SUB_1-FNUM])
        (Siapa, nonima), (pun, pun), (harus, adverbia), (siap, verba),
        (dicalonkan, verba), (untuk, konj_sub_tnp_koma_kt_pertama),
        (pilpres, nomina), (2024, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<pun>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_tnp_koma_1_kata_akhir_klausa_02(self):
        """
        -> S-P-O-PEL-F_KJ_SUB (FN-FV-FN-FPREP-[KJ_SUB-FN_KJ_SUB_YANG-FV])
        (Pihak, nomina), (kepolisian, nomina), (harus, adverbia),
        (mengusut, verba), (kasus, nomina), (ini, nomina), (dengan, dengan),
        (teliti, adjektiva), (agar, konj_sub_tnp_koma_kt_pertama), (tersangka, nomina),
        (yang, konj_sub_yang), (tidak, adverbia), (pernah, adverbia),
        (tertangkap, verba), (tersebut, verba), (dapat, adverbia), (diadili, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<dengan>",
            "<adjektiva>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<kj_sub_yang>",
            "<tidak>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_tnp_koma_2_kata_awal_klausa_01(self):
        """
        -> Kj Sub Tnp Koma 2 Kata Awal Klausa 01
        (Oleh, kj_sub_tnp_koma_kt_pertama), (karena, kj_sub_tnp_koma_kt_kedua),
        (pelanggaran, nomina), (yang, kj_sub_yang), (dilakukannya, verba),
        (,, td_koma), (ia, nomina), (harus, adverbia), (menunggu, verba),
        (di, preposisi), (lapangan, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_tnp_koma_kt_pertama>",
            "<kj_sub_tnp_koma_kt_kedua>",
            "<nomina>",
            "<kj_sub_yang>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_tnp_koma_2_kata_awal_klausa_02(self):
        """
        -> Kj Sub Tnp Koma 2 Kata Awal Klausa 02
        (Oleh, kj_sub_tnp_koma_kt_pertama), (karena, kj_sub_tnp_koma_kt_kedua),
        (kelalaiannya, nomina), (,, td_koma), (ia, nomina), (harus, adverbia),
        (menerima, verba), (penalti, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_tnp_koma_kt_pertama>",
            "<kj_sub_tnp_koma_kt_kedua>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_tnp_koma_2_kata_akhir_klausa_01(self):
        """
        -> Kj Sub Tnp Koma 2 Kata Akhir Klausa 01
        (Vincent, nomina), (dihukum, verba), (berdiri, verba),
        (di, preposisi), (lapangan, nomina), (oleh, kj_sub_tnp_koma_kt_pertama),
        (karena, kj_sub_tnp_koma_kt_kedua), (tindakannya, nomina),
        (yang, kj_sub_yang), (tidak, tidak), (terpuji, verba), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<kj_sub_tnp_koma_kt_kedua>",
            "<nomina>",
            "<kj_sub_yang>",
            "<tidak>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_tnp_koma_2_kata_akhir_klausa_02(self):
        """
        -> Kj Sub Tnp Koma 2 Kata Akhir Klausa 02
        (Ia, nomina), (sakit, adjektiva), (perut, nomina),
        (oleh, kj_sub_tnp_koma_kt_pertama), (sebab, kj_sub_tnp_koma_kt_kedua),
        (makan, verba), (gado-gado, nomina), (yang, kj_sub_yang),
        (sangat, adverbia), (pedas, adjektiva), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adjektiva>",
            "<nomina>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<kj_sub_tnp_koma_kt_kedua>",
            "<verba>",
            "<nomina>",
            "<kj_sub_yang>",
            "<adverbia>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_dengan_awal_klausa_01(self):
        """
        -> Kj Sub "Dengan" Awal Klausa 01
        (Dengan, dengan), (mengenakan, verba), (perlengkapan, nomina),
        (renang, verba), (,, td_koma), (anak, nomina), (pantai, nomina),
        (itu, nomina), (menyelam, verba), (di, preposisi), (lautan, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<dengan>",
            "<verba>",
            "<nomina>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_dengan_akhir_klausa_01(self):
        """
        -> Kj Sub "Dengan" Akhir Klausa 01
        (Polisi, nomina), (pergi, verba), (ke, preposisi), (lokasi, nomina),
        (kejadian, nomina), (dengan, dengan), (menggunakan, verba),
        (helikopter, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<dengan>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_demi_awal_klausa_01(self):
        """
        -> Kj Sub "Demi" Awal Klausa 01
        (Demi, demi), (menjaga, verba), (keadilan, nomina),
        (,, td_koma), (mereka, nomina), (menangkap, verba),
        (penjahat, nomina), (itu, nomina), (., td_akhir_kal)
        """
        kal = [
            "<demi>",
            "<verba>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_demi_akhir_klausa_01(self):
        """
        -> Kj Sub "Demi" Akhir Klausa 01
        (Mereka, nomina), (menangkap, verba), (penjahat, nomina),
        (itu, nomina), (demi, demi), (menjaga, verba),
        (keadilan, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<demi>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_obj_klausa_01(self):
        """
        -> S-P-O (N-V-[KJ_SUB_BAHWA-N-ADV-V])
        `(Presiden, nomina), (menyatakan, verba), (bahwa, konj_sub_bahwa),
        (reshuffling, nomina), (akan, adverbia), (dilakukan, verba),
        (., td_akhir_kal)`
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<kj_sub_bahwa>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_obj_klausa_02(self):
        """
        -> S-P-O_KLAUSA (FN-V-[KJ_SUB_BAHWA-N-FV-KJ_SUB-N])
        (Gubernur, nomina), (baru, adjektiva), (itu, nomina), (mengatakan, verba),
        (bahwa, konj_sub_bahwa), (dirinya, nomina), (akan, adverbia),
        (bersungguh-sungguh, verba), (bekerja, verba),
        (untuk, konj_sub_tnp_koma_kt_pertama), (rakyat, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adjektiva>",
            "<nomina>",
            "<verba>",
            "<kj_sub_bahwa>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_dgn_koma_awal_klausa_01(self):
        """
        -> Kj Sub Dgn Koma Awal Klausa 01
        (Bahkan, kj_sub_dgn_koma), (tanpa, adverbia), (uang, nomina),
        (pun, pun), (,, td_koma), (Ripto, nomina), (masih, adverbia),
        (tetap, adverbia), (hidup, verba), (nyaman, adjektiva),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_dgn_koma>",
            "<adverbia>",
            "<nomina>",
            "<pun>",
            "<td_koma>",
            "<nomina>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_dgn_koma_akhir_klausa_01(self):
        """
        -> S-P-F_KONJ_SUB (FN-FV-KJ_SUB-PREP-N_KJ_SUB_YANG)
        (Titik, nomina), (kumpul, nomina), (sudah, adverbia), (disepakati, verba),
        (,, td_koma), (yakni, kj_sub_dgn_koma), (di, preposisi), (lokasi, nomina),
        (yang, konj_subor), (telah, adverbia), (ditentukan, verba), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<td_koma>",
            "<kj_sub_dgn_koma>",
            "<preposisi>",
            "<nomina>",
            "<kj_sub_yang>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_berbeda_dengan_01(self):
        """
        -> Berbeda dengan (awal klausa) 01
        (Berbeda, kj_sub_berbeda), (dengan, dengan), (Indonesia, nomina),
        (,, td_koma), (sejumlah, nomina), (negara, nomina), (Eropa, nomina),
        (justru, adverbia), (melonggarkan, verba), (Prokes, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_berbeda>",
            "<dengan>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_berbeda_dengan_02(self):
        """
        -> Berbeda dengan (awal klausa) 02
        (Berbeda, kj_sub_berbeda), (dengan, dengan), (Indonesia, nomina),
        (dan, kj_koor_tak_hingga), (Thailand, nomina)
        (,, td_koma), (sejumlah, nomina), (negara, nomina), (Eropa, nomina),
        (justru, adverbia), (melonggarkan, verba), (Prokes, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_berbeda>",
            "<dengan>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_berbeda_dengan_03(self):
        """
        -> Berbeda dengan (awal klausa) 03
        (Berbeda, kj_sub_berbeda), (dengan, dengan), (Indonesia, nomina),
        (,, td_koma), (Malaysia, nomina), (,, td_koma),
        (dan, kj_koor_tak_hingga), (Thailand, nomina)
        (;, td_koma), (sejumlah, nomina), (negara, nomina), (Eropa, nomina),
        (justru, adverbia), (melonggarkan, verba), (Prokes, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_berbeda>",
            "<dengan>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_berbeda_dengan_04(self):
        """
        -> Berbeda dengan (akhir klausa) 01
        (Sejumlah, nomina), (negara, nomina), (Eropa, nomina), (justru, adverbia),
        (melonggarkan, verba), (Prokes, nomina), (,, td_koma), (berbeda, kj_sub_berbeda),
        (dengan, dengan), (Indonesia, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_koma>",
            "<kj_sub_berbeda>",
            "<dengan>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_berbeda_dengan_05(self):
        """
        -> Berbeda dengan (akhir klausa) 02
        (Sejumlah, nomina), (negara, nomina), (Eropa, nomina), (justru, adverbia),
        (melonggarkan, verba), (Prokes, nomina), (,, td_koma), (berbeda, kj_sub_berbeda),
        (dengan, dengan), (Indonesia, nomina), (dan, kj_koor_tak_hingga),
        (Thailand, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_koma>",
            "<kj_sub_berbeda>",
            "<dengan>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_sub_berbeda_dengan_06(self):
        """
        -> Berbeda dengan (akhir klausa) 03
        (Sejumlah, nomina), (negara, nomina), (Eropa, nomina), (justru, adverbia),
        (melonggarkan, verba), (Prokes, nomina), (,, td_koma), (berbeda, kj_sub_berbeda),
        (dengan, dengan), (Indonesia, nomina), (,, td_koma), (Malaysia, nomina),
        (,, td_koma), (dan, kj_koor_tak_hingga), (Thailand, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_koma>",
            "<kj_sub_berbeda>",
            "<dengan>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_salah_konj_sub_tnp_koma_01(self):
        """
        -> Test:Kj Sub Tnp Koma akhir klausa menggunakan koma.
        (Siapa, nonima), (pun, pun), (harus, adverbia), (siap, verba),
        (dicalonkan, verba), (,, td_koma), (untuk, konj_sub_tnp_koma_kt_pertama),
        (pilpres, nomina), (2024, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<pun>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<td_koma>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))

    def test_salah_konj_sub_dgn_koma_01(self):
        """
        -> Test:Kj Sub Dgn Koma akhir klausa tanpa koma.
        (Titik, nomina), (kumpul, nomina), (sudah, adverbia), (disepakati, verba),
        (yakni, kj_sub_dgn_koma), (di, preposisi), (lokasi, nomina),
        (yang, konj_subor), (telah, adverbia), (ditentukan, verba), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<verba>",
            "<kj_sub_dgn_koma>",
            "<preposisi>",
            "<nomina>",
            "<kj_sub_yang>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))
