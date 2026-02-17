import pygame
import os
import random
import sys
import asyncio
pygame.init()

# ---------- تعاریف حالت‌های بازی ----------
GAME_INTRO = "intro"
GAME_TIME_SETUP = "time_setup"
GAME_NORMAL = "normal"
GAME_DOOR_HIT = "door_hit"
GAME_IMAGE_VIEW = "image_view"
GAME_RESULT = "result"
GAME_END = "end"
game_state = GAME_INTRO

# ---------- مسیر فایل ----------
#BASE_DIR = os.path.dirname(__file__)
character_path = os.path.join( 'Character1\mohadeseh2.png')
door_path = os.path.join( 'Character1\dar1.png')
door_hit_path = os.path.join( 'Character1\dar2.png')
#BASE_DIR = os.path.dirname(__file__)
result_image_path = os.path.join( r'Character1\afarin.png')
stage4_background_path = os.path.join('Character1\stage4_background.png')
stage5_background_path = os.path.join( 'Character1\stage5_background.png')
stage6_background_path = os.path.join( 'Character1\stage6_background.png')
stage7_background_path = os.path.join('Character1\stage7_background.png')
# NEW: عکس‌های صفحات مقدماتی
intro_background_path = os.path.join('Character1\intro_background.png')
#BASE_DIR = os.path.dirname(__file__)
time_setup_background_path = os.path.join(r'Character1\time_setup_background.png')

# ---------- داده‌های عکس‌های سوال عمومی ----------
big_image_data = [
    {'path': os.path.join( 'Character1\solal1.png'), 'correct_answer': '2'},
    {'path': os.path.join( 'Character1\solal1_tow.png'), 'correct_answer': '7'},
    {'path': os.path.join('Character1\solal1_three.png'), 'correct_answer': '60'},
    {'path': os.path.join('Character1\solal1_four.png'), 'correct_answer': '6'}
]

# داده‌های عکس‌های سوال مخصوص مرحله 4
big_image_data_stage4 = [
    {'path': os.path.join( 'Character1\solal2_one.png'), 'correct_answer': '-4i'},
    {'path': os.path.join( 'Character1\solal2_tow.png'), 'correct_answer': '9i_-7j'},
    {'path': os.path.join('Character1\solal2_three.png'), 'correct_answer': '10i_-1'},
    {'path': os.path.join('Character1\solal2_four.png'), 'correct_answer': '4i_-6j'},
]

# داده‌های عکس‌های سوال مخصوص مرحله 6
big_image_data_stage6 = [
    {'path': os.path.join( 'Character1\solal3_one.png'), 'correct_answer': '5'},
    {'path': os.path.join('Character1\solal3_two.png'), 'correct_answer': '4'},
    {'path': os.path.join( 'Character1\solal3_three.png'), 'correct_answer': '12'},
    {'path': os.path.join('Character1\solal3_four.png'), 'correct_answer': '2'},
]

# ---------- صفحه ----------
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Adventure")

# ---------- رنگ‌ها ----------
GREEN = (0, 200, 0)
RED = (200, 0, 0)
SKY = (200, 230, 255)
BROWN = (139, 69, 19)
DARK_RED = (150, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
TURQUOISE = (64, 224, 208)
LIGHT_BLUE = (173, 216, 230)

# ---------- فونت ----------
font = pygame.font.SysFont('arial', 32)
input_font = pygame.font.SysFont('arial', 28)
big_font = pygame.font.SysFont('arial', 48)

# ---------- کاراکتر ----------
character_img = pygame.image.load(character_path)
character_img = pygame.transform.scale(character_img, (100, 120))

player_x = 100
player_y = 230
player_width = 60
player_height = 80

# ---------- در ----------
try:
    door_img_normal = pygame.image.load(door_path)
    door_img_normal = pygame.transform.scale(door_img_normal, (200, 230))
except:
    door_img_normal = pygame.Surface((200, 230))
    door_img_normal.fill(BROWN)
    pygame.draw.circle(door_img_normal, (255, 215, 0), (40, 40), 8)

try:
    door_img_hit = pygame.image.load(door_hit_path)
    door_img_hit = pygame.transform.scale(door_img_hit, (200, 230))
except:
    door_img_hit = pygame.Surface((200, 230))
    door_img_hit.fill(DARK_RED)
    pygame.draw.circle(door_img_hit, (255, 100, 0), (40, 40), 8)

# بارگذاری عکس نتیجه
try:
    result_image = pygame.image.load(result_image_path)
    result_image = pygame.transform.scale(result_image, (600, 400))
except:
    result_image = pygame.Surface((400, 200))
    result_image.fill((150, 150, 150))
    result_font = pygame.font.SysFont('arial', 36)
    text_surf = result_font.render("آفرین! پاسخ درست است", True, WHITE)
    text_rect = text_surf.get_rect(center=(200, 100))
    result_image.blit(text_surf, text_rect)

# بارگذاری عکس پس زمینه مرحله 4
try:
    stage4_background = pygame.image.load(stage4_background_path)
    stage4_background = pygame.transform.scale(stage4_background, (WIDTH, HEIGHT))
    print("✅ عکس پس زمینه مرحله 4 بارگذاری شد")
except:
    print("خطا در بارگذاری عکس پس زمینه مرحله 4")
    stage4_background = pygame.Surface((WIDTH, HEIGHT))
    stage4_background.fill((100, 50, 150))
    for i in range(10):
        star_x = random.randint(0, WIDTH)
        star_y = random.randint(0, HEIGHT - 100)
        pygame.draw.circle(stage4_background, (255, 255, 100), (star_x, star_y), 3)
    bg_font = pygame.font.SysFont('arial', 48)
    text_surf = bg_font.render("مرحله ویژه 4", True, WHITE)
    text_rect = text_surf.get_rect(center=(WIDTH//2, 50))
    stage4_background.blit(text_surf, text_rect)

# بارگذاری عکس پس زمینه مرحله 5
try:
    stage5_background = pygame.image.load(stage5_background_path)
    stage5_background = pygame.transform.scale(stage5_background, (WIDTH, HEIGHT))
    print("✅ عکس پس زمینه مرحله 5 بارگذاری شد")
except:
    print("خطا در بارگذاری عکس پس زمینه مرحله 5")
    stage5_background = pygame.Surface((WIDTH, HEIGHT))
    stage5_background.fill((0, 100, 150))
    for i in range(15):
        cloud_x = random.randint(0, WIDTH)
        cloud_y = random.randint(0, HEIGHT - 150)
        pygame.draw.ellipse(stage5_background, (200, 200, 255), (cloud_x, cloud_y, 60, 30))
        pygame.draw.ellipse(stage5_background, (200, 200, 255), (cloud_x+20, cloud_y-10, 50, 25))
    bg_font = pygame.font.SysFont('arial', 48)
    text_surf = bg_font.render("مرحله 5", True, WHITE)
    text_rect = text_surf.get_rect(center=(WIDTH//2, 50))
    stage5_background.blit(text_surf, text_rect)

# بارگذاری عکس پس زمینه مرحله 6
try:
    stage6_background = pygame.image.load(stage6_background_path)
    stage6_background = pygame.transform.scale(stage6_background, (WIDTH, HEIGHT))
    print("✅ عکس پس زمینه مرحله 6 بارگذاری شد")
except:
    print("خطا در بارگذاری عکس پس زمینه مرحله 6")
    stage6_background = pygame.Surface((WIDTH, HEIGHT))
    stage6_background.fill((80, 80, 80))
    for i in range(20):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 100)
        pygame.draw.rect(stage6_background, (150, 150, 150), (x, y, 5, 5))
    bg_font = pygame.font.SysFont('arial', 48)
    text_surf = bg_font.render("مرحله 6", True, WHITE)
    text_rect = text_surf.get_rect(center=(WIDTH//2, 50))
    stage6_background.blit(text_surf, text_rect)

# بارگذاری عکس پس زمینه مرحله 7 (پایان)
try:
    stage7_background = pygame.image.load(stage7_background_path)
    stage7_background = pygame.transform.scale(stage7_background, (WIDTH, HEIGHT))
    print("✅ عکس پس زمینه مرحله 7 بارگذاری شد")
except:
    print("خطا در بارگذاری عکس پس زمینه مرحله 7 - ساخت پس زمینه پیش‌فرض")
    stage7_background = pygame.Surface((WIDTH, HEIGHT))
    stage7_background.fill((255, 215, 0))
    bg_font = pygame.font.SysFont('arial', 72)
    text_surf = bg_font.render("پایان بازی", True, BLACK)
    text_rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    stage7_background.blit(text_surf, text_rect)
    text_surf2 = bg_font.render("🎉", True, BLACK)
    text_rect2 = text_surf2.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
    stage7_background.blit(text_surf2, text_rect2)
# NEW: بارگذاری عکس پس زمینه صفحه معرفی
try:
    intro_background = pygame.image.load(intro_background_path)
    intro_background = pygame.transform.scale(intro_background, (WIDTH, HEIGHT))
    print("✅ عکس پس زمینه صفحه معرفی بارگذاری شد")
except:
    print("خطا در بارگذاری عکس صفحه معرفی - ساخت پس زمینه پیش‌فرض")
    intro_background = pygame.Surface((WIDTH, HEIGHT))
    intro_background.fill(LIGHT_BLUE)
    bg_font = pygame.font.SysFont('arial', 48)
    text_surf = bg_font.render("به بازی ریاضی خوش آمدید!", True, BLACK)
    text_rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
    intro_background.blit(text_surf, text_rect)

# NEW: بارگذاری عکس پس زمینه صفحه تنظیم زمان
try:
    time_setup_background = pygame.image.load(time_setup_background_path)
    time_setup_background = pygame.transform.scale(time_setup_background, (WIDTH, HEIGHT))
    print("✅ عکس پس زمینه صفحه تنظیم زمان بارگذاری شد")
except:
    print("خطا در بارگذاری عکس صفحه تنظیم زمان - ساخت پس زمینه پیش‌فرض")
    time_setup_background = pygame.Surface((WIDTH, HEIGHT))
    time_setup_background.fill((200, 200, 150))
    bg_font = pygame.font.SysFont('arial', 48)
    text_surf = bg_font.render("زمان بازی را وارد کنید", True, BLACK)
    text_rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    time_setup_background.blit(text_surf, text_rect)

# ---------- متغیرهای عمومی ----------
current_big_image = None
door_positions = {
    2: 550,
    4: 550,
    6: 550
}
door_x = 550
door_y = 155
door_width = 50
door_height = 80
door_visible = False
# ---------- حالت‌های بازی ----------
game_state = GAME_INTRO
door_hit_timer = 0
DOOR_HIT_DURATION = 90
result_timer = 0

stage = 1
error_timer = 0

score = 0

end_timer = 180  # 3 ثانیه

user_text = ""
text_input_rect = pygame.Rect(150, 350, 500, 40)
text_input_active = True

clock = pygame.time.Clock()
running = True

custom_background_stages = [4, 5, 6, 7]

# NEW: متغیرهای مربوط به تایمر و تنظیمات
time_limit = 30          # پیش‌فرض
start_time = 0
remaining_time = 0
time_setup_text = "30"    # متن وارد شده در صفحه تنظیم زمان
time_setup_input_active = True
time_setup_input_rect = pygame.Rect(250, 320, 300, 40)  # کادر ورودی

# دکمه‌های صفحات مقدماتی
next_button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 100, 200, 50)  # دکمه "ادامه" در صفحه معرفی
start_game_button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 100, 200, 50)  # دکمه "شروع" در صفحه تنظیم
back_button_rect = pygame.Rect(20, 20, 100, 40)  # دکمه بازگشت به صفحه معرفی
button_xx = 340
button_yy= 350
button_widthh = 80
button_heighht = 50
next_button_rect = pygame.Rect(button_xx, button_yy, button_widthh, button_heighht)
button_x1 = 700
button_y2= 350
button_width1 = 80
button_height2 = 50
start_game_button_rect = pygame.Rect(button_x1, button_y2, button_width1, button_height2)
# دکمه فیروزه‌ای برای حرکت کاراکتر
button_x = 10
button_y = 60
button_width = 60
button_height = 30
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
# ---------- توابع ----------
def load_random_big_image(stage_number):
    try:
        if stage_number == 4:
            if big_image_data_stage4:
                random_item = random.choice(big_image_data_stage4)
                print(f"مرحله 4 - بارگذاری عکس: {os.path.basename(random_item['path'])}")
            else:
                random_item = random.choice(big_image_data)
                print(f"لیست مرحله 4 خالی - بارگذاری عکس: {os.path.basename(random_item['path'])}")
        elif stage_number == 6:
            if big_image_data_stage6:
                random_item = random.choice(big_image_data_stage6)
                print(f"مرحله 6 - بارگذاری عکس: {os.path.basename(random_item['path'])}")
            else:
                random_item = random.choice(big_image_data)
                print(f"لیست مرحله 6 خالی - بارگذاری عکس: {os.path.basename(random_item['path'])}")
        else:
            random_item = random.choice(big_image_data)
            print(f"مرحله {stage_number} - بارگذاری عکس: {os.path.basename(random_item['path'])}")
        
        img = pygame.image.load(random_item['path'])
        img = pygame.transform.scale(img, (500, 300))
        return img, random_item['correct_answer']
    except Exception as e:
        print(f"خطا در بارگذاری عکس: {e}")
        img = pygame.Surface((500, 300))
        if stage_number == 4:
            img.fill((150, 50, 200))
            fake_answers = ['20', '25', '30', '40']
            img_num = random.randint(1, len(fake_answers))
            answer = fake_answers[img_num-1]
            text_surf = font.render(f"مرحله ۴ - سوال #{img_num} - پاسخ: {answer}", True, WHITE)
        elif stage_number == 6:
            img.fill((80, 80, 150))
            fake_answers = ['50', '60', '7', '90']
            img_num = random.randint(1, len(fake_answers))
            answer = fake_answers[img_num-1]
            text_surf = font.render(f"مرحله ۶ - سوال #{img_num} - پاسخ: {answer}", True, WHITE)
        else:
            img.fill(random.choice([(100,100,200), (200,100,100), (100,200,100), (200,200,100)]))
            fake_answers = ['4', '8', '12', '16']
            img_num = random.randint(1, 4)
            answer = fake_answers[img_num-1]
            text_surf = font.render(f"سوال #{img_num} - پاسخ: {answer}", True, WHITE)
        text_rect = text_surf.get_rect(center=(250, 150))
        img.blit(text_surf, text_rect)
        return img, answer

def show_result(is_correct, user_answer=""):
    global result_text, result_color, result_timer, current_big_image, current_correct_answer, stage, score
    
    if is_correct:
        result_text = "آفرین!"
        result_color = GREEN
        score += 1
        print(f"✅ آفرین! امتیاز: {score}")
        stage += 1
        result_timer = 120
        return True
    else:
        result_text = "اشتباه!"
        result_color = RED
        score -= 1
        print(f"❌ اشتباه! امتیاز: {score}")
        current_big_image, current_correct_answer = load_random_big_image(stage)
        return False
# ---------- تابع اصلی ----------
async def main():
    global running, player_x, stage, score, user_text, text_input_active, door_hit_timer, result_timer, game_state
    global remaining_time, start_time, time_setup_text, time_setup_input_active, error_timer
    
    clock = pygame.time.Clock()
    
    while running:
        dt = clock.tick(60)
        current_ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ===== صفحه معرفی =====
            if game_state == GAME_INTRO:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if next_button_rect.collidepoint(event.pos):
                        game_state = GAME_TIME_SETUP
                        time_setup_text = "30"
# ===== صفحه تنظیم زمان =====
            elif game_state == GAME_TIME_SETUP:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        time_setup_text = time_setup_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            time_limit = int(time_setup_text)
                            if time_limit <= 0:
                                time_limit = 30
                        except:
                            time_limit = 30
                        start_time = current_ticks
                        remaining_time = time_limit
                        game_state = GAME_NORMAL
                        stage = 1
                        score = 0
                        player_x = 100
                        user_text = ""
                    else:
                        if event.unicode.isdigit() and len(time_setup_text) < 5:
                            time_setup_text += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if time_setup_input_rect.collidepoint(event.pos):
                        time_setup_input_active = True
                    else:
                        time_setup_input_active = False
                    if start_game_button_rect.collidepoint(event.pos):
                        try:
                            time_limit = int(time_setup_text)
                            if time_limit <= 0:
                                time_limit = 30
                        except:
                            time_limit = 30
                        start_time = current_ticks
                        remaining_time = time_limit
                        game_state = GAME_NORMAL
                        stage = 1
                        score = 0
                        player_x = 100
                        user_text = ""
                    if back_button_rect.collidepoint(event.pos):
                        game_state = GAME_INTRO
# ===== سایر حالت‌های بازی =====
            else:
                # دکمه فیروزه‌ای
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_rect.collidepoint(event.pos) and game_state == GAME_NORMAL:
                        player_x += 100
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and game_state == GAME_NORMAL:
                        player_x += 100

                if game_state == GAME_RESULT:
                    if event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN):
                        game_state = GAME_NORMAL
                        user_text = ""

                elif game_state == GAME_IMAGE_VIEW:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_state = GAME_NORMAL
                            user_text = ""
                        elif event.key == pygame.K_RETURN:
                            user_input = user_text.strip()
                            if user_input == current_correct_answer:
                                if show_result(True):
                                    game_state = GAME_RESULT
                            else:
                                show_result(False)
                                user_text = ""
                                text_input_active = True
                        elif event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            if len(user_text) < 30:
                                user_text += event.unicode
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        text_input_active = text_input_rect.collidepoint(event.pos)

                elif game_state == GAME_NORMAL:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        error_timer = 25

                elif game_state == GAME_END:
                    if event.type == pygame.KEYDOWN:
                        running = False
# ===== تایمرها =====
        if game_state == GAME_RESULT:
            result_timer -= 1
            if result_timer <= 0:
                game_state = GAME_NORMAL
                user_text = ""

        if game_state == GAME_DOOR_HIT:
            door_hit_timer -= 1
            if door_hit_timer <= 0:
                current_big_image, current_correct_answer = load_random_big_image(stage)
                game_state = GAME_IMAGE_VIEW
                user_text = ""
                text_input_active = True

        # ===== محاسبه زمان باقی‌مانده =====
        if game_state in [GAME_NORMAL, GAME_DOOR_HIT, GAME_IMAGE_VIEW, GAME_RESULT]:
            elapsed = (current_ticks - start_time) / 1000.0
            remaining_time = max(0, time_limit - elapsed)
            if remaining_time <= 0 and game_state != GAME_END:
                game_state = GAME_END
                print("⏰ زمان تمام شد!")
        # ===== حرکت در حالت عادی =====
        if game_state == GAME_NORMAL:
            speed = 4 + stage
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= speed
            if keys[pygame.K_RIGHT]:
                player_x += speed

            door_visible = stage in [2, 4, 6]
            if stage in door_positions:
                door_x = door_positions[stage]

            if door_visible:
                player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
                door_rect = pygame.Rect(door_x, door_y, door_width, door_height)
                if player_rect.colliderect(door_rect):
                    game_state = GAME_DOOR_HIT
                    door_hit_timer = DOOR_HIT_DURATION
                    if player_x + player_width > door_x:
                        player_x = door_x - player_width

            if player_x > 720:
                stage += 1
                player_x = 100
                print(f"🎮 وارد مرحله {stage} شدیم!")
                if stage >= 7:
                    game_state = GAME_END
                    print("🎉 بازی به پایان رسید! 🎉")
# ===== رسم =====
        if game_state == GAME_INTRO:
            screen.blit(intro_background, (0, 0))
            pygame.draw.rect(screen, TURQUOISE, next_button_rect, border_radius=10)
            pygame.draw.rect(screen, BLACK, next_button_rect, 2, border_radius=10)
            next_text = font.render("Next", True, BLACK)
            screen.blit(next_text, next_text.get_rect(center=next_button_rect.center))

        elif game_state == GAME_TIME_SETUP:
            screen.blit(time_setup_background, (0, 0))
            pygame.draw.rect(screen, WHITE, time_setup_input_rect, 2)
            pygame.draw.rect(screen, (240,240,240) if time_setup_input_active else (200,200,200),
                             time_setup_input_rect.inflate(-4,-4))
            text_surf = input_font.render(time_setup_text, True, BLACK)
            screen.blit(text_surf, (time_setup_input_rect.x+10, time_setup_input_rect.y+10))
            pygame.draw.rect(screen, GREEN, start_game_button_rect, border_radius=10)
            pygame.draw.rect(screen, BLACK, start_game_button_rect, 2, border_radius=10)
            start_text = font.render("play", True, BLACK)
            screen.blit(start_text, start_text.get_rect(center=start_game_button_rect.center))
            pygame.draw.rect(screen, RED, back_button_rect, border_radius=5)
            pygame.draw.rect(screen, BLACK, back_button_rect, 2, border_radius=5)
            back_text = font.render("return", True, WHITE)
            screen.blit(back_text, back_text.get_rect(center=back_button_rect.center))

        else:
# سایر حالت‌های بازی
            if stage == 4:
                screen.blit(stage4_background, (0, 0))
            elif stage == 5:
                screen.blit(stage5_background, (0, 0))
            elif stage == 6:
                screen.blit(stage6_background, (0, 0))
            elif stage == 7 or game_state == GAME_END:
                screen.blit(stage7_background, (0, 0))
            else:
                screen.fill(SKY)

            if game_state == GAME_NORMAL:
                if stage not in custom_background_stages:
                    pygame.draw.rect(screen, GREEN, (0, 340, WIDTH, 60))
                if door_visible:
                    screen.blit(door_img_normal, (door_x, door_y))
                screen.blit(character_img, (player_x, player_y))

                stage_text_color = WHITE if stage in custom_background_stages else BLACK
                stage_text = font.render(f"Stage: {stage}", True, stage_text_color)
                screen.blit(stage_text, (10, 10))

                time_color = RED if remaining_time < 10 else (YELLOW if stage in custom_background_stages else BLACK)
                time_text = font.render(f"Time: {int(remaining_time)}s", True, time_color)
                time_rect = time_text.get_rect(midtop=(WIDTH//2, 10))
                screen.blit(time_text, time_rect)

                score_text = font.render(f"Score: {score}", True, YELLOW if stage in custom_background_stages else BLACK)
                score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
                screen.blit(score_text, score_rect)

                if error_timer > 0:
                    overlay = pygame.Surface((WIDTH, HEIGHT))
                    overlay.set_alpha(120)
                    overlay.fill(RED)
                    screen.blit(overlay, (0, 0))
                    error_timer -= 1

            elif game_state == GAME_DOOR_HIT:
                if stage not in custom_background_stages:
                    pygame.draw.rect(screen, GREEN, (0, 340, WIDTH, 60))
                screen.blit(door_img_hit, (door_x, door_y))
                screen.blit(character_img, (player_x, player_y))

                countdown = door_hit_timer // 60 + 1
                #countdown_text = font.render(f"سوال در {countdown}...", True, WHITE)
                #countdown_rect = countdown_text.get_rect(center=(WIDTH//2, 50))
                #screen.blit(countdown_text, countdown_rect)
                stage_text_color = WHITE if stage in custom_background_stages else SKY
                stage_text = font.render(f"Stage: {stage}", True, stage_text_color)
                screen.blit(stage_text, (10, 10))

                time_text = font.render(f"Time: {int(remaining_time)}s", True, YELLOW)
                time_rect = time_text.get_rect(midtop=(WIDTH//2, 10))
                screen.blit(time_text, time_rect)

                score_text = font.render(f"Score: {score}", True, YELLOW if stage in custom_background_stages else WHITE)
                score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
                screen.blit(score_text, score_rect)

            elif game_state == GAME_IMAGE_VIEW:
                overlay = pygame.Surface((WIDTH, HEIGHT))
                overlay.set_alpha(200)
                overlay.fill((0, 0, 0))
                screen.blit(overlay, (0, 0))

                pygame.draw.rect(screen, WHITE, text_input_rect, 2)
                pygame.draw.rect(screen, SKY if not text_input_active else (200, 230, 255),
                                text_input_rect.inflate(-4, -4))

                if current_big_image:
                    big_image_rect = current_big_image.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
                    screen.blit(current_big_image, big_image_rect)

                stage_text = font.render(f"Stage: {stage}", True, WHITE)
                screen.blit(stage_text, (10, 10))

                time_text = font.render(f"Time: {int(remaining_time)}s", True, YELLOW)
                time_rect = time_text.get_rect(midtop=(WIDTH//2, 10))
                screen.blit(time_text, time_rect)

                score_text = font.render(f"Score: {score}", True, YELLOW)
                score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
                screen.blit(score_text, score_rect)

                text_surface = input_font.render(user_text, True, BLACK)
                screen.blit(text_surface, (text_input_rect.x + 10, text_input_rect.y + 10))

                if text_input_active and pygame.time.get_ticks() % 1000 < 500:
                    cursor_x = text_input_rect.x + 10 + text_surface.get_width()
                    pygame.draw.line(screen, BLACK,
                                   (cursor_x, text_input_rect.y + 10),
                                   (cursor_x, text_input_rect.y + 30), 2)

            elif game_state == GAME_RESULT:
                overlay = pygame.Surface((WIDTH, HEIGHT))
                overlay.set_alpha(150)
                overlay.fill((0, 0, 0))
                screen.blit(overlay, (0, 0))
                result_rect = result_image.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.blit(result_image, result_rect)

                score_text = font.render(f"Score: {score}", True, YELLOW)
                score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 120))
                screen.blit(score_text, score_rect)

                time_text = font.render(f"Time: {int(remaining_time)}s", True, YELLOW)
                time_rect = time_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
                screen.blit(time_text, time_rect)

                if result_timer > 0:
                    stage7_background = pygame.image.load(stage7_background_path)
                    stage7_background = pygame.transform.scale(stage7_background, (WIDTH, HEIGHT))

                score_end = font.render(f"Score: {score}", True, YELLOW)
                score_end_rect = score_end.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
                screen.blit(score_end, score_end_rect)

            # رسم دکمه فیروزه‌ای
            if game_state not in [GAME_INTRO, GAME_TIME_SETUP]:
                pygame.draw.rect(screen, TURQUOISE, button_rect, border_radius=8)
                pygame.draw.rect(screen, (0, 150, 150), button_rect, 2, border_radius=8)
                button_text = font.render("--->", True, BLACK)
                text_rect = button_text.get_rect(center=button_rect.center)
                screen.blit(button_text, text_rect)

        pygame.display.update()
        await asyncio.sleep(0)

# ---------- اجرای برنامه ----------
if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
    sys.exit()

