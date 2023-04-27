import unittest
from cfg_initialization import cfg_true_or_false


class TestAposSuple(unittest.TestCase):
    def test_suple_depan_01(self):
        """
        -> F_SUP-S-P-O ([FPREP-KOMA]-N-FV-N)
        (Atas, preposisi), (perhatian, nomina), (Saudara, nomina),
        (,, td_koma), (kami, nomina), (ucapkan, verba), (terima, verba),
        (kasih, nomina), (., td_akhir_kal)
        """
        kal = [
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_depan_02(self):
        """
        -> F_SUP-P-S ([V-FN-KOMA]-FV-FN)
        (ditambah, verba), (kelalaian, nomina), (protokol, nomina), (kesehatan, nomina),
        (,, td_koma), (pasti, adjektiva), (dapat, adverbia), (menyebabkan, verba),
        (kenaikan, nomina), (covid-19, nomina), (., td_akhir_kal)
        """
        kal = [
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<adjektiva>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_depan_03(self):
        """
        -> F_SUP-S-P-O-F_KJ_SUB ([N-FV-KOMA]-N-FV-FN-[KJ_SUB-N-FNUM-F_KJ_YANG])
        (Dirinya, nomina), (tak, adverbia), (mau, adverbia), (ambil, verba),
        (pusing, verba), (,, td_koma), (Ian, nomina), (pun, pun), (siap, verba),
        (melanjutkan, verba), (grup, nomina), (band, nomina), (Radja, nomina),
        (tanpa, konj_sub_tnp_koma_kt_pertama), (adanya, nomina), (dua, numeralia),
        (sahabatnya, nomina), (yang, konj_sub_yang), (telah, adverbia),
        (hengkang, verba), (itu, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<pun>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<numeralia>",
            "<nomina>",
            "<kj_sub_yang>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_depan_04(self):
        """
        -> F_SUPLE-S-P-O ([N-KOMA]-FN-V-FN)
        (Menurutnya, nomina), (,, td_koma), (perombakan, nomina), (kabinet, nomina),
        (merupakan, verba), (kewenangan, nomina), (Presiden, nomina), (Jokowi, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_depan_05(self):
        """
        -> F_SUPLE-APOS-S-P-PEL ([FN-APOS-V-KOMA]-FN-ADJ-[N-V-N-FPREP-F_KJ_SUB_YANG])
        (Kabid, nomina), (Litbang, nomina), (PP, nomina), (The, nomina),
        (Jakmania, nomina), (,, td_koma), (Afrizal, nomina),
        (Kasriyanto, nomina), (mengatakan, verba), (,, td_koma),
        (The, nomina), (Jakmania, nomina), (yakin, adjektiva),
        (persija, nomina), (bisa, verba), (menang, verba),
        (dari, preposisi), (bali, nomina), (united, nomina),
        (yang, konj_sub_yang), (kini, nomina), (bertengger, verba),
        (di, preposisi), (posisi, nomina), (lima, numeralia),
        (klasemen, nomina), (liga, nomina), (1, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<adjektiva>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<kj_sub_yang>",
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<numeralia>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_depan_06(self):
        """
        -> [F_SUPLE-APOS]-S-P-O-PEL ([FN-APOS-V]-FN-V-N-FPREP)
        (Marlinda, nomina), (Vasty, nomina), (Overbeek, nomina), (,, td_koma),
        (ahli, nomina), (informatika, nomina), (tim, nomina), (U-Tapis, nomina),
        (sekaligus, adverbia), (ketua, nomina), (prodi, nomina), (teknik, nomina),
        (informatika, nomina), (UMN, nomina), (,, td_koma), (mengatakan, verba),
        (,, td_koma), (tim, nomina), (prodi, nomina), (Informatika, nomina), (UMN, nomina),
        (menghadapi, verba), (tantangan, nomina), (dalam, preposisi), (crawling, nomina),
        (data, nomina), (dan, kj_koor_tak_hingga), (pra, nomina), (proses, nomina),
        (sistem, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<verba>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_tengah_01(self):
        """
        -> Suplementasi Tengah 01
        (Kongres, nomina), (Bahasa, nomina), (Indonesia, nomina), (IX, numeralia),
        (,, td_koma), (diikuti, verba), (oleh, preposisi), (peserta, nomina),
        (dari, preposisi), (dalam, nomina), (dan, kj_koor_tak_hingga), (luar, nomina),
        (negeri, nomina), (,, td_koma), (telah, adverbia), (menghasilkan, verba),
        (rumusan, nomina), (bagi, preposisi), (pengembangan, nomina),
        (dan, kj_koor_tak_hingga), (pembinaan, nomina), (bahasa, nomina),
        (dan, kj_koor_tak_hingga), (sastra, nomina), (Indonesia, nomina),
        (dan, kj_koor_tak_hingga), (daerah, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<td_koma>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_tengah_02(self):
        """
        -> Suplementasi Tengah 02
        (Makassar, nomina), ('(', kurung_buka), (terkenal, verba), (dengan, dengan),
        (sebutan, nomina), (Kota, nomina), (Angin, nomina), (Mamiri, nomina),
        (')', kurung_tutup), (menjadi, verba), (pusat, nomina), (pengembangan, nomina),
        (wilayah, nomina), (Indonesia, nomina), (Timur, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<kurung_buka>",
            "<verba>",
            "<dengan>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<kurung_tutup>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_tengah_03(self):
        """
        -> Suplementasi Tengah 03
        (Orang, nomina), (itu, nomina), (--, td_tengah_kal), (konon, adverbia),
        (selalu, adverbia), (mendapat, verba), (peringkat, nomina), (satu, numeralia),
        (ketika, kj_sub_tnp_koma_kt_pertama), (menjadi, verba), (taruna, nomina),
        (--, td_tengah_kal), (terpilih, verba), (sebagai, kj_sub_tnp_koma_kt_pertama),
        (tokoh, nomina), (berbahasa, verba), (Indonesia, nomina), (terbaik, adjektiva),
        (pada, preposisi), (tahun, nomina), (2003, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<td_tengah_kal>",
            "<adverbia>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<verba>",
            "<nomina>",
            "<td_tengah_kal>",
            "<verba>",
            "<kj_sub_tnp_koma_kt_pertama>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<adjektiva>",
            "<preposisi>",
            "<nomina>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_belakang_01(self):
        """
        -> S-P-O-F_SUPLE (N-V-FN-F_KURUNG)
        (Obama, nomina), (menjadi, verba), (presiden, nomina), (Amerika, nomina),
        ('(', kurung_buka), (hal, nomina), (yang, konj_sub_yang), (tidak, adverbia),
        (pernah, adverbia), (terbayangkan, verba), (sebelumnya, nomina), (')',
        kurung_tutup), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<kurung_buka>",
            "<nomina>",
            "<kj_sub_yang>",
            "<tidak>",
            "<adverbia>",
            "<verba>",
            "<nomina>",
            "<kurung_tutup>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_belakang_02(self):
        """
        -> Suplementasi Belakang 02
        (Mereka, nomina) (mengadakan, verba), (Kongres, nomina), (Bahasa, nomina),
        (Indonesia, nomina), (IX, numeralia), (,, td_koma), (diikuti, verba),
        (oleh, preposisi), (peserta, nomina), (dari, preposisi), (dalam, nomina),
        (dan, kj_koor_tak_hingga), (luar, nomina), (negeri, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<td_koma>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_suple_belakang_03(self):
        """
        -> Suplementasi Belakang 03
        (Musisi, nomina), (itu, nomina), (menyindir, verba), (perilaku, nomina),
        (pejabat, nomina), (melalui, verba), (lagu-lagu, nomina), (yang, kj_sub_yang),
        (diciptakannya, verba), (--, td_tengah_kal), (dan, kj_koor_tak_hingga),
        (saya, nomina), (setuju, verba), (dengan, dengan), (cara, nomina), (itu, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<kj_sub_yang>",
            "<verba>",
            "<td_tengah_kal>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<verba>",
            "<dengan>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_salah_suple_belakang_01(self):
        """
        -> Tes: Suplementasi akhir kal dengan koma menggunakan frasa konjungsi.
        (Musisi, nomina), (itu, nomina), (menyindir, verba), (perilaku, nomina),
        (pejabat, nomina), (melalui, verba), (lagu-lagu, nomina), (yang, kj_sub_yang),
        (diciptakannya, verba), (,, td_koma), (dan, kj_koor_tak_hingga),
        (saya, nomina), (setuju, verba), (dengan, dengan), (cara, nomina), (itu, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<kj_sub_yang>",
            "<verba>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<verba>",
            "<dengan>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))
