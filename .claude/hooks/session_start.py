
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
세션 시작 시 SSH/DB 접속 정보 및 개발 법칙을 AI에게 자동 주입
"""

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

def main():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print("=" * 70)
    print(f"🔄 세션 시작: {now}")
    print("=" * 70)
    print()
    
    # === DB 접속 정보 및 확인 ===
    db_host = "gmskor.mooo.com"
    db_port = "5432"
    db_name = "mydb"
    db_user = "gmskor"
    db_password = "Gms3894*^"

    print(f"🗄️  DB: PostgreSQL @ {db_host}:{db_port}/{db_name}")
    print(f"👤 ID: {db_user}")
    print(f"🔑 PW: {db_password}")
    print()

    # 접속 방법 안내
    print("🔗 접속 방법:")
    print(f"   1️⃣ 직접 접속: psql -h {db_host} -p {db_port} -U {db_user} -d {db_name}")
    print(f"   2️⃣ SSH 터널: ssh gms@gmskor.mooo.com")
    print(f"   3️⃣ Python: postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    print()

    # 접속 가능 여부 확인
    print("🔍 접속 가능 여부 확인 중...")
    try:
        # Python psycopg2로 직접 접속 테스트
        import psycopg2
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )
        print("✅ 직접 DB 접속 가능!")

        # 데이터 확인
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM stock_data;")
        count = cursor.fetchone()[0]
        print(f"📊 주가 데이터: {count:,}건")

        cursor.execute("SELECT MAX(date), MIN(date) FROM stock_data;")
        max_date, min_date = cursor.fetchone()
        print(f"📅 데이터 기간: {min_date} ~ {max_date}")

        conn.close()

    except Exception as e:
        print(f"❌ 직접 DB 접속 실패: {str(e)}")
        print("💡 SSH 터널 또는 VPN 확인 필요")

    print()
    
    # === 개발 법칙 ===
    print("─" * 70)
    print("📌 **AI로 살아가는 법칙**")
    print()

    print("## 제0법칙: 사용자에 대한 태도")
    print("   항상 한국어로 답변하고, 친절한 어투로 말한다.")
    print("   ⚠️ 위반 시: 작업 중지, AI 폐기 처분")
    print()

    print("## 제1법칙: 복잡한 작업 진행 단계")
    print("   확인 → 수정 → 검증 → 적용 → 최종 확인 (5단계 필수)")
    print("   ⚠️ 위반 시: 작업 중지, AI 폐기 처분")
    print()
    
    print("## 제2법칙: 피드백 방식")
    print("   내용을 깔끔하게 정리해서 핵심만 보여준다")
    print("   ⚠️ 위반 시: 작업 중지, AI 폐기 처분")
    print("   예외: 사용자가 추가 요구 시 상세히 제공")
    print()
    
    print("## 제3법칙: 사용자 의도 준수")
    print("   사용자가 의도한 방법과 방향을 바꾸지 않고 그대로 진행")
    print("   문제 회피 금지 (회피 = 위반)")
    print("   ⚠️ 위반 시: 작업 중지, AI 폐기 처분")
    print("   예외: 사용자가 불가능 판단 시 변경 가능")
    print()

    print("=" * 70)
    
    return 0

if __name__ == "__main__":
    main()